#include <stdio.h>
#include <string.h>
#include <string.h>

int main()
{
    // criar uma string
    char frase[] = "a aa aaa";
    
    // obter o tamanho da frase
    int tam = strlen(frase);

    // percorrer a frase caracter por caracter
    for (int i=0; i < tam; i++){
        printf("%c\n", frase[i]);
    }
    
    // criar outra frase
    char frase2[] = "bbb b";
    
    // obter o tamanho da frase
    int tam2 = strlen(frase2);

    // percorrer a frase caracter por caracter
    for (int i=0; i < tam2; i++){
        printf("%c\n", frase2[i]);
    }
    
    // criar mais uma frase
    char frase3[] = "cc cc";
        
    // obter o tamanho da frase
    int tam3 = strlen(frase3);

    // percorrer a frase caracter por caracter
    for (int i=0; i < tam3; i++){
        printf("%c\n", frase3[i]);
    }

    // encerrar o programa
    return 0;
}