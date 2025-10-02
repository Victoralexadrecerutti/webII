#include <stdio.h>
#include <string.h>

// definir uma função que exiba a frase com um caracter em cada linha
void mostrar_por_linha(char frase[]) {
    // obter o tamanho da frase
    int tam = strlen(frase);

    // percorrer a frase caracter por caracter
    for (int i=0; i < tam; i++){
        printf("%c\n", frase[i]);
    }
}

int main()
{
    // mostrar uma frase por linha
    mostrar_por_linha("a aa aaa");

    // mostrar outra frase por linha
    mostrar_por_linha("bbb b");

    // mostra mais uma frase por linha
    mostrar_por_linha("cc cc");
    
    // encerrar o programa
    return 0;
}