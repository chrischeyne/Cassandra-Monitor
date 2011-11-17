/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.jointhegrid.hadoopjmx;

/**
 *
 * @author ecapriolo
 */
public class JMXBaseException extends Exception{
  public JMXBaseException(Exception e){
    super(e);
  }
  public JMXBaseException(String s,Exception e){
    super(s,e);
  }
  public JMXBaseException(String s){
    super(s);
  }

}
