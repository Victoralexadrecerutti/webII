/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package mutex;


public class TestarThreadModificaContador {
  
    public static void main(String[] args) {
        
        // criar threads
        ThreadModificaContador t1 = new ThreadModificaContador("T1");
        ThreadModificaContador t2 = new ThreadModificaContador("T2");
        ThreadModificaContador t3 = new ThreadModificaContador("T3");
        
        // iniciar
        t1.start();
        t2.start();
        t3.start();
    }
}
