# https://www.w3schools.com/python/python_arrays.asp
# python não suporta vetores, mas listas podem ser usadas

# declara uma lista
numbers = []

# repete 10 vezes
# pode utilizar apenas 1 número no "range", nesse caso
# será equivalente a variar i de 0 a 9 
# (para i=10 não entra no loop)
for i in range(10):
    # pede um número
    n = input("Digite um número: ")
    # guarda o número na lista
    numbers.append(n)
    
# percorre o vetor e mostra os números
for i in range(10):
    print(f"vetor[{i}] = {numbers[i]}")    