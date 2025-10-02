# criar uma string
linha = 'João da Silva,josilva@gmail.com,47 9 9234 5678'
# quebrar a string usando vírgula
partes = linha.split(",")
# percorrer as partes (for each)
for p in partes:
    # mostrar a parte
    print(p)
# mostrar o email (parte 2 da string)
print(f'Email: {partes[1]}')