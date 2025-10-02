# https://matplotlib.org/stable/tutorials/pyplot.html
# https://www.w3schools.com/python/matplotlib_scatter.asp

import matplotlib.pyplot as plt

# pontos em x
x = [1, 2, 3, 4, 5, 6, 7, 8]
# pontos em y
y = [1, 2, 3, 4, 8, 4, 8, 4]

# constrói o gráfico
plt.scatter(x, y)
# mostra o gráfico
plt.show()