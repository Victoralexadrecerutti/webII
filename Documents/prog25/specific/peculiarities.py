# --------------------------------------------------------------------------------
# PECULIAR 00: python é interpretado, mas exibe verificação em tempo de compilação
# CORRIGIR ERRO deste PROGRAMA linha XXX
# --------------------------------------------------------------------------------

# ----------------------------------------------------------------
# PECULIAR 01: listas, tuplas, strings, tipos mutáveis e imutáveis
# ----------------------------------------------------------------

lista = [] # lista vazia
lista2 = [1, 2, 3]
tupla = () # tupla vazia
n = (1+2) # n não é uma tupla!
print(n) # 3
t = (1+2,) # precisa da vírgula para que t seja uma tupla
print(t) # (3,)
tupla2 = (1, 2, 3)
tupla3 = 4, 5, 6 # definindo tuplas apenas com vírgulas! tupla = (4, 5, 6)
print(tuple(lista2)) # convertendo: (1, 2, 3)
print(list(tupla3)) # converteu de novo: [4, 5, 6]

def inclui_na_lista_e_mostra(elemento, lista):
    lista.append(elemento)
    print(lista)
    return lista

lista = inclui_na_lista_e_mostra("Primeiro", []) # ['Primeiro']
lista = inclui_na_lista_e_mostra("Segundo", lista) # ['Primeiro', 'Segundo']
inclui_na_lista_e_mostra("Terceiro", lista) # ['Primeiro', 'Segundo', 'Terceiro'] => passagem por referência

# define função sem retorno => usar passagem por referência
def inclui_e_mostra(elemento, parametro_lista):
  parametro_lista.append(elemento) # continua modificando a lista por referência
  print(parametro_lista)

lista = [] 
inclui_e_mostra("Primeiro", lista) # ['Primeiro']
inclui_e_mostra("Segundo", lista) # ['Primeiro', 'Segundo']
inclui_e_mostra("Terceiro", lista) # ['Primeiro', 'Segundo', 'Terceiro']

tupla = () 
try:
    tupla.append("Primeiro")
    print("Consegui inserir na tupla!")
except:
    print("Não foi possível inserir na tupla") # <= VAI ACONTECER ESSA SITUAÇÃO

# PORQUE?
# PORQUE?
# PORQUE?

# lista é MUTÁVEL => pode ser ALTERADA :-)
# tupla é IMUTÁVEL => NÃO pode ser ALTERADA :-(

frase = "O amanhã sempre vem" # string é IMUTÁVEL
print(frase)
print(frase.replace("vem", "virá")) # O amanhã sempre virá
print(frase) # a frase permanece original! O amanhã sempre vem

frase2 = "outra frase"
# essa string foi redefinida, mas não alterada

lista = ['lembrando: ','listas ','são ','mutáveis, ','cuidado']
print(lista) # ['lembrando: ', 'listas ', 'são ', 'mutáveis, ', 'cuidado']
print(lista.remove("são ")) # o método remove não retorna valor (mostra "None")
print(lista) # o elemento foi removido! ['lembrando: ', 'listas ', 'mutáveis, ', 'cuidado'] 

a = "Pedro"
b = a # copiou, e não referenciou, pois string é imutável! <== AMAZING
b = "Maria"
print(a, b) # Pedro Maria

'''

a ------> "Pedro"

b ------> "Pedro"

'''

lista = [1, 2, 3]
outra = lista # referenciou, pois lista é mutável! <== AWESOME
outra.remove(3)
print(outra) # [1, 2]
print(lista) # removeu da lista também! [1, 2]

'''

lista -------> [1,2,3]
                  ^
outra ------------|

'''

lista = ['a', 'b', 'c']
outra = lista.copy() # copiou um tipo mutável
outra.remove('b') # removeu apenas da cópia :-)
print(outra) # ['a', 'c']
print(lista) # permanece intacta: ['a', 'b', 'c']

# tudo certo abaixo
lista = ['lobo','tubarao']
def adicionar_perfil(elemento, conjunto):
    conjunto.append(elemento)
    return conjunto
lista = adicionar_perfil('aguia', lista)
print(lista) # ['lobo', 'tubarao', 'aguia']
lista = adicionar_perfil('gato', lista)
print(lista) # ['lobo', 'tubarao', 'aguia', 'gato']

# tornando o parâmetro opcional: inserindo um valor padrão
def incluir_perfil(elemento, conjunto=[]): # o parâmetro conjunto é opcional
    conjunto.append(elemento)
    return conjunto

comeco = ['tem alguem']
print(incluir_perfil('lobo', comeco)) # ['tem alguem', 'lobo']
print(incluir_perfil('tubarao')) # ['tubarao']
print(incluir_perfil('aguia')) # ['tubarao', 'aguia'] ==> AMAZING 2
print(incluir_perfil('gato')) # ['tubarao', 'aguia', 'gato']

# o valor padrão do parâmetro é avaliado em tempo de definição,
# e assim considera-se a mesma referência para o parâmetro,
# desde a primeira vez que a função é utilizada
# além disso, o parâmetro é MUTÁVEL!

# como acessar esse parâmetro reutilizado?
print("acessando o parâmetro reutilizado por meio de atribuição")
me_da_o_parametro = incluir_perfil('ovelha')
print(me_da_o_parametro) # ['tubarao', 'aguia', 'gato', 'ovelha']

    
# esse fenômeno de reaproveitamento não ocorre para tuplas (imutáveis), 
# já que é preciso criar outras referências para fazer as conversões
def incluir_animal(elemento, conjunto=()):
    l = list(conjunto)
    l.append(elemento)
    return tuple(l)
print(incluir_animal('lobo')) # ('lobo',)
print(incluir_animal('tubarao')) # ('tubarao',)

# se informar o parâmetro opcional, ok!
def adicionar_animal(elemento, conjunto=()):
    l = list(conjunto)
    l.append(elemento)
    return tuple(l)
print(incluir_animal('tubarao',('lobo',))) # ('lobo', 'tubarao')
print(incluir_animal('aguia',('lobo','tubarao'))) # ('lobo', 'tubarao', 'aguia')

# --------------------------------
# PECULIAR 02: escopo de variáveis
# --------------------------------

sorte = 7
def numero_da_sorte():
    return sorte
print(numero_da_sorte()) # 7

def mudar_numero_da_sorte():
    sorte = 13 # criou outra variável local chamada sorte
print(numero_da_sorte()) # 7
mudar_numero_da_sorte()
print(numero_da_sorte()) # 7!!!

azar = 15
def mostrar_numero_azar():
    print(azar) 
mostrar_numero_azar() # 15

try:
    azar = 8
    def tentar_mostrar_numero_azar():
        print(azar) # erro: usando variável local antes da definição
        azar = 13 # tenta consertar o número do azar :-)
    tentar_mostrar_numero_azar()
except:
    print("ERRO!")

# => python interpreta declaração por declaração, e não linha por linha
# usar global é uma saída, mas não é uma boa prática

mundo = "belo"
def mostrar_mundo():
    # global mundo # DESCOMENTAR ESSA LINHA PARA RESOLVER O ERRO NESTE PROGRAMA XXX
    print(mundo) # mostra: belo
    mundo = "grande" # muda o mundo 
    print(mundo) # mostra: grande
print("* uso do global")    
mostrar_mundo() 




# --------------------
# OUTROS PECULIARIDADES...
# --------------------

# https://py.checkio.org/blog/10-common-beginner-mistakes-in-python/
# https://www.devmedia.com.br/python-estrutura-condicional-if-else/38217
# https://www.pythonforbeginners.com/basics/string-manipulation-in-python
# https://py.checkio.org/blog/10-common-beginner-mistakes-in-python/

# elif
# if com estrutura similar a um switch case
#
idade = 18 # define-se uma variável de controle
if idade < 12:
    print('criança')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')

#
# print
#

nome = "Pedro"
print("Nome:",nome) # mostra 'Nome: Pedro'; a vírgula insere um espaço!
print("Nome:"+nome) # mostra: 'Nome:Pedro'
# sep e end valem, por padrão: ' ' (espaço) e '\n', respectivamente
print("que", "mensagem", "legal", sep=" :-) ", end='\n\n\nFIM\n')
# saída: 
'''
que :-) mensagem :-) legal


FIM
'''

#
# for percorrendo lista com posições numéricas e por elemento
#
pessoas = ['Joao','Maria','Jose','Hans'] # lista a percorrer

# percorrendo a lista por posição numérica
tamanho_lista = len(pessoas) # obtém o tamanho da lista
# i varia de zero até o tamanho da lista menos 1 (de zero a 3 neste exemplo)
# equivalente a range(0, tamanho_lista)
for i in range(tamanho_lista): 
    print("Mostrando:",pessoas[i])

# percorrendo a lista por elemento (sem informação de posição)
for atual in pessoas: # cada pessoa será mapeada na variável ``atual''
    print("Exibindo:",atual)  

# o range captura desde o valor inicial até o valor final menos 1
# exibir: 0, 1, 2, 3, 4
for i in range(5):
    print(i) 

# fazer uma lista com 5 números
print(list(range(0, 5))) # [0, 1, 2, 3, 4]

# faixa com passo negativo
# range(inicial, final, passo)
print(list(range(10, 1, -2))) # [10, 8, 6, 4, 2]

#
# while, break, continue
#
i = 0
while i < 20: 
    i+=1 # (i = i + 1) python não suporta i++ ou ++i
    print("\nanalisando:",i, end='') # imprime sem EOF
    info = "" # informações a serem mostradas

    if i == 8:
        print(" ESTE É O NÚMERO 8, INCRÍVEL")
        continue # vai para o fim do laço; não executa o if abaixo
        
    if i % 17 == 0: # interrompe o laço se for divisível por 17
        print(" FIM")
        break
    elif i % 2 == 0: # é divisível por 2?
        info += " [é par!]"
    else:
        info = " ok"
    print(info, end='')

#
# manipulação de strings
#
frase = "Esta.frase.vai.ser.mostrada.em.partes"
print(frase[0]) # mostra o primeiro caracter da frase
print(frase[:10]) # mostra 10 primeiros caracteres
print(frase[-9:]) # mostra os 9 últimos caracteres
print(frase[::3]) # mostra caracteres saltando a cada 3
print(frase.split(".")) # converte para lista quebrada por "."
print(frase.find("frase")) # mostra a posição da palavra "frase"
print(frase.replace(".","+")) # substitui ponto por soma
print(frase * 2) # mostra a frase duas vezes
print(2 + 2,"=> isso é um número!")
print("2" + "2", "=> isso é uma string")
print("Tamanho da frase:", len(frase))
print("Quantos pontos tem na frase?", frase.count("."))
print(" ".join(frase)) # insere um espaço entre cada caracter da frase

#
# formatação de strings
# https://www.python-course.eu/python3_formatted_output.php
# 
s = "* formato: Pedro tem {0:.2f} metros de altura".format(1.7321)
print(s)

cpf = "12345678910" # cpf 
s = f"* formato: Mariana tem CPF {cpf} e tirou {7.12:2.1f} em inglês"
print(s)
print("* CPF:", cpf)
y = cpf[-11:-8],cpf[-8:-5],cpf[-5:-2] # converte para tupla; resultado: ('123', '456', '789')
x = ".".join(y) + "-" + cpf[-2:] # insere "." antes de cada elemento de y, depois concatena
print("* formato: " + x) # 123.456.789-10

#
# diversos
#
# exit(): interrompe um programa!
# pep8: leitura complementar: https://www.python.org/dev/peps/pep-0008/