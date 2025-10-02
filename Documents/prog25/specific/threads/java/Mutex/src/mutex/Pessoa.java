/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package mutex;

public class Pessoa {

    String nome;
    String email;

    public Pessoa(String n, String e) {
        this.nome = n;
        this.email = e;
    }

    @Override
    public String toString() {
        return this.nome + " - " + this.email;
    }
}
