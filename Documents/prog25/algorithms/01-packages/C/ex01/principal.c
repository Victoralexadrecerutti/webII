#include <stdio.h>
#include "biblioteca.h"

int main() {
    int a = 10;
    int b = 20;
    int x = somar_inteiros(a, b);
    printf("Soma: %d\n", x);
    return 0;
}

/*

Executing:

$ gcc biblioteca.c principal.c -o principal
$ ./principal

*/