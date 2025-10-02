# criar uma string
frase = "Olá tudo bem com você"

# percorrer a frase caracter por caracter
for c in frase:
    # mostrar o caracter em uma linha nova
    print(c)

# remover os acentos da frase
frase = frase.replace('á','a')
frase = frase.replace('ê', 'e')

# mostrar a frase modificada
print(frase)