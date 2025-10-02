#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>

// https://www.freecodecamp.org/news/how-to-find-length-of-c-string-with-examples/

int main()
{
    // declarar vetor de caracteres de tamanho fixo
    char frase[100];
    // inserir uma string no vetor de caracteres
    strcpy(frase,"Olá tudo bem com você");
    // obter o tamanho "ocupado" do vetor
    int tam = strlen(frase);

    // outra forma de criar um vetor de caracteres
    char frase2[] = "Tudo certo";

    //  obter o tamanho o segundo vetor
    int tam2 = strlen(frase2);
    
    // mostrar os tamanhos
    printf("tamfrase1=%d tamfrase2=%d\n", tam, tam2);
    
    // percorrer o vetor de caracteres
    for (int i=0; i < tam; i++){
        printf("%c ", frase[i]);
    }
    // imprimir uma quebra de linha
    printf("\n");

    // percorrer o outro vetor de caracteres
    for (int i=0; i < tam2; i++){
        printf("%c ", frase2[i]);
    }
    // imprimir uma quebra de linha
    printf("\n");

    // string em C termina com operador \0
    
    // remover os acentos da frase
    frase[2] = 'a';
    frase[3] = ' ';
    frase[21] = 'e';
    frase[22] = ' ';

    for (int i=0; i < tam; i++){
        printf("%c ", frase[i]);
    }
    // imprimir uma quebra de linha
    printf("\n");

    // encerrar o programa
    return 0;
}