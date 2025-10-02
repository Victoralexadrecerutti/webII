from libs.mymath import *
from libs.mysplit import *

a = 10
b = 20
x = somar_inteiros(a,b)
print(f'Soma: {x}')


texto = "Mary,ma@gmail.com,47922334455,Brazil"
n = count_parts(texto, ",")
print(f"partes: {n}")
p = get_part(texto, ",", 2)
print(f"parte 2: {p}")