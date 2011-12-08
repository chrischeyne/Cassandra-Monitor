/*
* Copyright 2009 Edward Capriolo
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*   http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
 */
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.jointhegrid.hadoopjmx;

import java.io.IOException;
import java.net.MalformedURLException;
import java.util.HashMap;
import java.util.Map;
import javax.management.AttributeNotFoundException;
import javax.management.InstanceNotFoundException;
import javax.management.IntrospectionException;
import javax.management.MBeanException;
import javax.management.MBeanInfo;
import javax.management.MBeanServerConnection;
import javax.management.MalformedObjectNameException;
import javax.management.ObjectName;
import javax.management.ReflectionException;
import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;


/**
 * No one class will every be capable of connecting to a JMX Server extracting
 * and presenting all relevent JMX information in a format usable for all
 * NMS systems. JMXBase provides a simple model to specify the information a user
 * is interested in, fetch it, store it and output it. Cacti and Nagios easily
 * integrate with JMX Base.
 * @author ecapriolo
 */
public class JMXBase {
  /** The URL of the JMXServer to aquire data from*/
  protected String jmxURL;
  /** The jmx user credential (you need rw to call operations)*/
  protected String user;
  protected String pass;
  protected String objectName;
  protected String [] wantedVariables;
  protected String [] wantedOperations;
  protected JMXOutput output = null;
  protected Map<String,Object> wantedVarResults = null;
  protected Map<String,Object> wantedOperResults = null;

  protected JMXConnector connector;
  protected MBeanServerConnection connection;
  protected JMXServiceURL jmxUrl;

  public JMXBase(){
    output=new JMXOutput();
    wantedOperations = new String []{};
    wantedVariables = new String []{};
    wantedVarResults = new HashMap<String,Object>();
    wantedOperResults = new HashMap<String,Object>();
  }

  public JMXBase(MBeanServerConnection conn){
    this();
    connection=conn;
  }

  public void fetch() throws JMXBaseException {
    if (connection == null){
      makeConnection();
    }
    //if we have data we are re-fetching it
    this.wantedVarResults.clear();
    this.wantedOperResults.clear();

    for (String var:this.wantedVariables){
      Object theResult= getObjectAttribute(this.objectName,var);
      this.wantedVarResults.put(var, theResult);
    }

    for (String op : wantedOperations) {
      Object theResult = invokeOperation(this.objectName,op);
      this.wantedOperResults.put(op,theResult);
    }

  }

  public void output() throws JMXBaseException {
    
    for (String var:this.wantedVariables){
      System.out.print( 
              output.output(var, this.getWantedVarResultsRO().get(var) ) );
    }

    for (String op : wantedOperations) {
      System.out.println(
              output.output(op, this.getWantedOperResultsRO().get(op) ) );
    }

  }

  public Object invokeOperation( String objectName, String operation)
          throws JMXBaseException{
    Object result = null;
    try {
      ObjectName on = new ObjectName(objectName);
      result = connection.invoke(on, operation, new Object[]{}, new String[]{});

    } catch (InstanceNotFoundException ex){
      throw new JMXBaseException(ex);
    } catch (MalformedObjectNameException ex){
      throw new JMXBaseException(ex);
    } catch (MBeanException ex){
      throw new JMXBaseException(ex);
    }  catch (ReflectionException ex){
      throw new JMXBaseException(ex);
    } catch (IOException ex){
      throw new JMXBaseException(ex);
    }
    return result;
  }
  public Object getObjectAttribute(String objectName, String attribute)
          throws JMXBaseException {
    Object result=null;
    try {
      ObjectName on = new ObjectName(objectName);
      MBeanInfo info = connection.getMBeanInfo(on);
      Object attr2 = connection.getAttribute(on, attribute);
      if (attr2==null){
        throw new JMXBaseException(attribute+" not found in "+objectName);
      } else {
        result = attr2;
      }
    } catch (InstanceNotFoundException ex){
      throw new JMXBaseException(ex);
    } catch (MalformedObjectNameException ex){
      throw new JMXBaseException(ex);
    } catch (IntrospectionException ex){
      throw new JMXBaseException(ex);
    } catch (MBeanException ex){
      throw new JMXBaseException(ex);
    } catch (AttributeNotFoundException ex){
      throw new JMXBaseException(ex);
    } catch (ReflectionException ex){
      throw new JMXBaseException(ex);
    } catch (IOException ex){
      throw new JMXBaseException(ex);
    }
    return result;
  }

  public void setup(String [] args){

    if (System.getProperty("jmxURL")!= null)
      setJmxURL( System.getProperty("jmxURL") );
    if (System.getProperty("jmxUser")!= null)
      setUser(System.getProperty("jmxUser") );
    if (System.getProperty("jmxPass")!= null)
      setPass(System.getProperty("jmxPass") );
    if (System.getProperty("jmxObject")!= null)
      setObjectName(System.getProperty("jmxObject"));

    if (args.length >= 3) {
      setJmxURL(args[0]);
      setUser(args[1]);
      setPass(args[2]);
    }
    if (args.length >=4){
      setObjectName(args[3]);
    }
    
  }
  
  public void makeConnection() throws JMXBaseException {
    try {
      jmxUrl = new JMXServiceURL(this.jmxURL);
      Map m = new HashMap();
      m.put(JMXConnector.CREDENTIALS, new String[]{this.user, this.pass});
      connector = JMXConnectorFactory.connect(jmxUrl, m);
      connection = connector.getMBeanServerConnection();
    } catch (MalformedURLException ex){
      throw new JMXBaseException (ex);
    } catch (IOException  ex){
      throw new JMXBaseException (ex);
    }
  }

  public void closeConnection() throws JMXBaseException{
    try {
      connector.close();
    } catch (IOException ex){
      throw new JMXBaseException (ex);
    }
  }

  public Map<String,Object> getWantedVarResultsRO(){
    return java.util.Collections.unmodifiableMap(wantedVarResults);
  }

  public Map<String,Object> getWantedOperResultsRO(){
    return java.util.Collections.unmodifiableMap(wantedOperResults);
  }

  public MBeanServerConnection getConnection() {
    return connection;
  }

  public void setConnection(MBeanServerConnection connection) {
    this.connection = connection;
  }

  public String getObjectName() {
    return objectName;
  }

  public void setObjectName(String objectName) {
    this.objectName = objectName;
  }

  public String getPass() {
    return pass;
  }

  public void setPass(String pass) {
    this.pass = pass;
  }

  public String getUser() {
    return user;
  }

  public void setUser(String user) {
    this.user = user;
  }

  public String getJmxURL() {
    return jmxURL;
  }

  public void setJmxURL(String jmxURL) {
    this.jmxURL = jmxURL;
  }

  class Output  {
   
  }
}