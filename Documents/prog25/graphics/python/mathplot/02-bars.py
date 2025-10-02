# https://www.w3schools.com/python/matplotlib_bars.asp

import matplotlib.pyplot as plt
import numpy as np

# valores em x
x = ["A", "B", "C", "D", "E", "F", "G", "H"]
# barras em y
y = [1, 2, 3, 4, 8, 4, 8, 4]

# constrói o gráfico
plt.bar(x,y)

# exibe o gráfico
plt.show()