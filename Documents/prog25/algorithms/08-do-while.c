// https://www.freecodecamp.org/news/python-do-while-loop-example/

#include <stdio.h>

int main()
{
    // inicializa um indice (i) com zero
    int i = 0;
    // comece
    do
    {
        // mostre o número i
        printf("i = %i\n", i);
        // incremente i
        i = i + 1;

    // repita enquanto i < 10
    } while (i < 10);
    return 0;
}