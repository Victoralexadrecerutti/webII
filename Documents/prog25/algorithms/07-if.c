#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // sorteia um número entre 1 e 10

    // passo 1: semente de geração de números aleatórios
    srand(time(NULL));

    // passo 2: escolhe um número aleatório
    int n = rand();

    // passo 3: obtém o resto para delimitar
    // uma faixa; por exemplo, entre 1 e 10
    int a = (n % 10) + 1;

    // sorteia outro número entre 1 e 10
    n = rand();
    int b = (n % 10) + 1;

    // se a for maior do que b
    if (a < b)
        // mostre a e depois b
        printf("%d, %d\n", a, b);
    // senao
    else
        // mostre b e depois a
        printf("%d, %d\n", b, a);
}
