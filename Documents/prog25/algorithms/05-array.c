// https://www.w3schools.com/c/c_arrays.php

#include <stdio.h>

int main()
{
    // declara um vetor para até 10 números
    int numbers[10];
    // repete 10 vezes
    for (int i=0; i <=9; i++) {
        // pede um número
        printf("Digite um número: ");
        int n;
        scanf("%d", &n);
        // guarda o número em uma posição de vetor
        numbers[i] = n;
    }
    
    // percorre o vetor e mostra os números
    for (int i=0; i <=9; i++) {
        printf("vetor[%d] = %d\n", i, numbers[i]);
    }
    return 0;
}