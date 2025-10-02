import random

# sorteia um número entre 1 e 10
a = random.randint(1, 10)

# sorteia outro número entre 1 e 10
b = random.randint(1, 10)

# se a for maior do que b
if a < b:
    # mostre a e depois b
    print(f"{a},{b}");
# senao
else:
    # mostre b e depois a
    print(f"{b},{a}");