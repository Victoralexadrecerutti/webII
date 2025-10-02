#include <stdio.h>
#include <string.h>
#include "mysplit.h"

/* return the position of the delimiter in the string
update the "ret" with the substring

example:

- phrase to be breaked:
char frase[100] = "Mary,ma@gmail.com,47922334455,Brazil";
    
- count how many parts there are, using delimiter ",":
int n = count_parts(frase, ",");

- get the second part into nte variable "parte", using delimiter ",":
char parte[100];
get_part(frase, ",", 2, parte);

*/

int internal_my_get_part(char string2[], char delimiter[], char *ret)
{

    // printf("recebi: %s\n", string2);

    // storing in another variable, in order to make it works!
    // something about type conversion
    char string[100];
    strcpy(string, string2);

    // pointer to found the delimiter
    char *pv;

    // find the first occurrency
    pv = strstr(string, delimiter);
    if (pv != NULL)
    {
        // get the part position
        long int pos = pv - string;

        // printf("Posição da parte 1: %ld\n", pos);

        // temporary variable
        char temp[100] = "";

        // get the part in the temp, quantity=pos
        memcpy(temp, &string, pos);
        // find the insere final de string
        temp[pos] = '\0';

        // printf("parte: %s", temp);

        strcpy(ret, temp);

        return pos;
    }
    else
    {
        // put all the string in the ret
        strcpy(ret, string);
        return 0;
    }
}


int count_parts(char string3[], char delimiter[])
{
    char frase[100];
    strcpy(frase, string3);

    char vem[100];

    // parts counter
    int count = 0;

    int pos = 1;
    while (pos > 0)
    {
        count++;

        pos = internal_my_get_part(frase, ",", vem);
        // printf("===> %s em %d\n", vem, pos);

        // size of the nem string
        int ns = sizeof(frase) - pos;
        // update the string
        for (int i = 0; i < ns; i++)
        {
            frase[i] = frase[i + pos + 1];
        }
        // memcpy( frase, &frase+pos);
        // printf("NOVA frase: %s\n", frase);
    }
    return count;
}

// retorna a n_part-esima parte (começando de 1)
void get_part(char string3[], char delimiter[], int n_part, char *ret)
{
    // adapting the parameter
    char frase[100];
    strcpy(frase, string3);

    // temp for getting the part
    char vem[100];

    // parts counter
    int count = 0;

    char temp[100] = "";

    int pos = 1;
    while (pos > 0)
    {
        count++;

        pos = internal_my_get_part(frase, ",", vem);
        // printf("===> %s em %d\n", vem, pos);

        // size of the nem string
        int ns = sizeof(frase) - pos;
        // update the string
        for (int i = 0; i < ns; i++)
        {
            frase[i] = frase[i + pos + 1];
        }

        if (count == n_part)
        {
            // get the part in the temp, quantity=pos
            //memcpy(temp, &frase, pos);
            // find the insere final de string
            //temp[pos] = '\0';

            strcpy(ret, vem);
        }
        // printf("parte: %s", temp);
        
    }

}
