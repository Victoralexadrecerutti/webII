# função que conta quantas partes tem uma string,
# conforme certo delimitador
def count_parts(frase, delim):
    # quebra a frase por partes
    tmp = frase.split(delim)
    # retorna o tamanho do vetor de partes
    return len(tmp)
    # contribuição do Clóvis (para testar)
    # return frase.count(delim)+1

# função que retorna uma parte de string
def get_part(frase, delim, i):
    # quebra a frase por partes
    tmp = frase.split(delim)
    # retorna a i-esima parte (começando de 1)
    return tmp[i-1]

# só executa o código abaixo se 
# o programa que estiver sendo executado for este
if __name__ == "__main__":
    # teste da biblioteca
    texto = "Mary,ma@gmail.com,47922334455,Brazil"
    n = count_parts(texto, ",")
    print(f"partes: {n}")
    p = get_part(texto, ",", 2)
    print(f"parte 2: {p}")