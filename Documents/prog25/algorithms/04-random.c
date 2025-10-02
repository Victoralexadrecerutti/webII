#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main()
{
    // escolha um número entre 1 e 10

    // passo 1: semente de geração de números aleatórios
    srand(time(NULL));

    // passo 2: escolhe um número aleatório
    int n = rand();

    // passo 3: obtém o resto para delimitar
    // uma faixa; por exemplo, entre 1 e 10
    int i = (n % 10) + 1;

    // mostre o número sorteado
    printf("%d\n", i);
}