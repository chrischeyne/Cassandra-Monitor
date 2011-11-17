/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.jointhegrid.hadoopjmx;

/**
 *
 * @author ecapriolo
 */
public class JMXOutput {
  public JMXOutput(){}
  public String output(String var, Object value){
    return var+":"+value+" ";
  }
}
