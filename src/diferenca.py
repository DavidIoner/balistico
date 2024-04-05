import math
import matplotlib.pyplot as plt
import numpy as np

# Inicialização das variáveis
Vi = 950.0  # Velocidade inicial (m/s)
theta = 25.0  # Ângulo de lançamento (em graus)
m = 9.5  # Massa do projétil (kg)
D = 0.01  # Coeficiente de arrasto

# Função para calcular a trajetória
def calcular_trajetoria(Vi, theta, m, D):
    dt = 0.01  # Passo de tempo
    g = 9.8  # Aceleração da gravidade
    t = 0.0  # Tempo inicial
    x = [0.0]  # Posição horizontal inicial
    y = [0.0]  # Posição vertical inicial
    Vx = Vi * math.cos(math.radians(theta))  # Velocidade horizontal inicial
    Vy = Vi * math.sin(math.radians(theta))  # Velocidade vertical inicial

    while y[-1] >= 0.0:
        v = math.sqrt(Vx ** 2 + Vy ** 2)
        Dx = -D * v * Vx
        Dy = -D * v * Vy

        Vx += (Dx / m) * dt
        Vy += ((Dy / m) - g) * dt

        x.append(x[-1] + Vx * dt)
        y.append(y[-1] + Vy * dt)

        t += dt

    return x, y


def trajetoria_atual(theta):
    dt = 0.01  # Passo de tempo
    t = 0.0  # Tempo inicial
    x = [0.0]  # Posição horizontal inicial
    y = [0.0]  # Posição vertical inicial
    dset = theta - 0.5
    ang = np.radians(dset)
    while t < 3100:
        t += dt
        x.append(x[-1] + np.cos(ang) * dt)
        y.append(y[-1] + np.sin(ang) * dt)

    return x, y


# Criar a figura e os eixos
fig, ax = plt.subplots()

a, b = trajetoria_atual(theta)
ax.plot(a, b, color="red", label="BT-46")
# Calcular a trajetória inicial
x, y = calcular_trajetoria(Vi, theta, m, D)

# Plotar a trajetória inicial
ax.plot(x, y, label="Atualização", color="blue")

# Remover labels dos eixos
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)

# Definir aspecto igual para os eixos
ax.set_aspect('equal')

# Remover título
plt.title("")

# Remover bordas
ax.axis('off')
ax.legend(loc="upper left")
# Salvar o gráfico como svg com fundo transparente, sem as labels, somente o gráfico
plt.savefig("trajetoria.png", transparent=True, bbox_inches="tight", pad_inches=0)

plt.show()
