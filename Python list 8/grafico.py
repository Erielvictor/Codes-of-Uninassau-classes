import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = np.linspace(-3, 3, 100)
# Valores correspondentes de y
y = 2 * x

# Criação do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x', color='b')
plt.scatter([-2, -1, 0, 1, 2], [-4, -2, 0, 2, 4], color='red')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico da função y = 2x')
plt.xlabel('x')
plt.ylabel('y')

# Adicionar grade e legenda
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
