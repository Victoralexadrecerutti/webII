#include <stdio.h>
#include <string.h>

int main () {
    char linha[100] = "1999,\"Acre\",\"Janeiro\",9,1999-01-01";
    char *tmp; // guarda a última parte da string que foi cortada (variável temporária)
    char *partes[10]; // onde todas as partes são armazenadas juntas
    int i = 0;

    // pega a primeira parte da string até a vírgula e guarda na variável tmp
    tmp = strtok(linha, ",");

    // faz isso até que não tenham mais partes para serem cortadas ou o array fique cheio
    while (tmp != NULL && i < 10) {
        // guarda a parte cortadada no array de partes
        partes[i] = tmp;
        // corta a próxima parte
        i++;
        tmp = strtok(NULL, ",");
    }

    // mostra as partes uma por uma
    for (int j = 0; j < i; j++) {
        printf("Parte %d: %s\n", j, partes[j]);
    }

    // mostra o ano e a quantidade de incêndios
    printf("Ano: %s, Incendios: %s\n", partes[0], partes[3]);

    return 0;
}