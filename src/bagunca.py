import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Criação da figura e dos eixos
fig, ax = plt.subplots()

# Plota o primeiro gráfico (linha azul)
ax.plot(x, y1, color="blue", label="Gráfico 1")

# Plota o segundo gráfico (linha vermelha)
ax.plot(x, y2, color="red", label="Gráfico 2")

# Adiciona uma legenda
ax.legend()

# Exibe a plotagem
plt.show()
