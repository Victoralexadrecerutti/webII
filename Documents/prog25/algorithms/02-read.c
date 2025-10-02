#include <stdio.h>

int main()
{
    printf("Digite um número: ");
    int n;
    scanf("%d", &n);
    int p = n * n;
    printf("%d ao quadrado é: %d\n", n, p);
    return 0;
}