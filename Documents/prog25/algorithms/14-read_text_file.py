# ler dados do arquivo .csv
# os dados ficam em arquivo texto, 
# separados por vírgula (comma-separated values - CSV)

# se existir o arquivo de dados
f = open("14-dados.csv", "r")
if f:
    # ler o arquivo linha por linha
    for linha in f:
        # mostra a linha
        print(linha)

    # fechar o arquivo
    f.close()
else:
    print("O arquivo de dados ainda não existe, nenhum dado foi lido")