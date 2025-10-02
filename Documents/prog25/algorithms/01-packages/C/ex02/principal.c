#include <stdio.h>
#include "libs/mysplit.h"
#include "libs/mymath.h"

int main() {
    // using math function
    int a = 10;
    int b = 20;
    int x = somar_inteiros(a, b);
    printf("Soma: %d\n", x);

    // using split function
    char frase[] = "Mary,ma@gmail.com,47922334455,Brazil";
    int n = count_parts(frase, ",");
    printf("partes: %d\n", n);
    char parte[100];
    get_part(frase, ",", 2, parte);
    printf("parte 2: %s\n", parte);

    return 0;
}

/*

Executing:

$ gcc principal.c libs/* -o principal
$ ./principal

Referência interessante para leitura:
https://stackoverflow.com/questions/1496313/returning-a-c-string-from-a-function

*/