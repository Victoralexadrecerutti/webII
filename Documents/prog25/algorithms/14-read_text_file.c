#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// ler dados do arquivo .csv
// os dados ficam em arquivo texto, 
// separados por vírgula (comma-separated values - CSV)

int main()
{
    // variável temporária para ler cada linha
    char buffer[250];

    // se existir o arquivo de dados
    FILE *fp;
    fp = fopen("14-dados.csv", "r");
    if (fp != NULL)
    {
        // ler o arquivo linha por linha
        while (fgets(buffer, 250, fp))
        {
            // mostra a linha
            printf("%s", buffer);
        }

        // fechar o arquivo
        fclose(fp);
    }
    else
    {
        printf("O arquivo de dados ainda não existe, nenhum dado foi lido\n");
    }
    
    // encerrar o programa
    return 0;
}