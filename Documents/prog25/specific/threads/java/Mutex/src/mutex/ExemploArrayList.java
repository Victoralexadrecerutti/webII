/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package mutex;

import java.util.ArrayList;

public class ExemploArrayList {
    
    public static void main(String[] args) {
        
        // criar um arraylist de strings
        ArrayList<String> animais = new ArrayList();
        
        // adicionar animais
        animais.add("Gato");
        animais.add("Cachorro");
        animais.add("Elefante");
        
        // percorrer o arraylist
        for (String s : animais) {
            // listar o animal atual
            System.out.println(s);
        }
        
        // criar um arraylist de pessoas
        ArrayList<Pessoa> pessoas = new ArrayList();
        
        // adicionar pessoas
        pessoas.add(new Pessoa("João", "jo@gmail.com"));
        pessoas.add(new Pessoa("Maria", "ma@gmail.com"));
        
        // percorrer o arraylist
        for (Pessoa p : pessoas) {
            // listar a pessoa
            System.out.println(p);
        }
    }
}