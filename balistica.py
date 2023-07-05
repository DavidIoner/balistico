import math

import matplotlib.pyplot as plt


def calcular_trajetoria(Vi, theta, m, D):
    # Variáveis iniciais
    dt = 0.01  # Passo de tempo
    g = 9.8  # Aceleração da gravidade
    t = 0.0  # Tempo inicial
    x = [0.0]  # Posição horizontal inicial
    y = [0.0]  # Posição vertical inicial
    Vx = Vi * math.cos(math.radians(theta))  # Velocidade horizontal inicial
    Vy = Vi * math.sin(math.radians(theta))  # Velocidade vertical inicial

    while y[-1] >= 0.0:
        # Cálculo do arrasto
        v = math.sqrt(Vx ** 2 + Vy ** 2)
        Dx = -D * v * Vx
        Dy = -D * v * Vy

        # Atualização das velocidades
        Vx += (Dx / m) * dt
        Vy += ((Dy / m) - g) * dt

        # Atualização das posições
        x.append(x[-1] + Vx * dt)
        y.append(y[-1] + Vy * dt)

        # Atualização do tempo
        t += dt

    return x, y


# Parâmetros do projétil
Vi = 950.0  # Velocidade inicial (m/s)
theta = 15.0  # Ângulo de lançamento (em graus)
m = 9.5  # Massa do projétil (kg)
D = 0.5  # Coeficiente de arrasto

# Cálculo da trajetória
x, y = calcular_trajetoria(Vi, theta, m, D)

# Plotagem da trajetória
plt.plot(x, y)
plt.xlabel("Distância (m)")
plt.ylabel("Altura (m)")
plt.title("Trajetória do Projétil")
plt.show()
