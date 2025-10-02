/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package mutex;

// https://www.baeldung.com/java-mutex

import java.util.Random;

public class ThreadModificaContador extends Thread {

    // gerador de números aleatórios
    static Random gerador = new Random();

    // número acessado por todas as threads
    // precisa ser static para todas as threads usarem o mesmo
    static int n = 0;

    // meu mutex :-)
    // precisa ser static para todas as threads usarem o mesmo
    static Object mut = new Object();

    // "nome" da thread
    String myid;

    // construtor da thread com parâmetro
    public ThreadModificaContador(String desc) {
        this.myid = desc;
    }

    // corpo da thread
    @Override
    public void run() {

        //  repete x vezes
        for (int q = 0; q < 2; q++) {

            // gera um número entre 0 e 10
            int i = gerador.nextInt(10);

            // se fos ímpar, inverte sinal para diminuir
            if (i % 2 != 0) {
                i *= -1;
            }
            
            // REGIÃO CRÍTICA
            synchronized (mut) {

                // altera n
                n += i;

                // mostrar novo valor e informações de quem mexeu
                System.out.printf("%d %s, sorteado: %d, novo n = %d \n",
                        q, this.myid, i, n);

            }
            // espera 3 segundos (3000 milisegundos)
            try {
                Thread.sleep(3000);
            } catch (InterruptedException ex) {
                System.out.print("sleep interronpido\n");
            }
        }
    }
}
