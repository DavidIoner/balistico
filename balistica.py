import math

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Inicialização das variáveis
Vi = 950.0  # Velocidade inicial (m/s)
theta = 20.0  # Ângulo de lançamento (em graus)
m = 9.5  # Massa do projétil (kg)
D = 0.05  # Coeficiente de arrasto

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


# Função para atualizar o gráfico
def atualizar_grafico(event):
    # Obter os valores atualizados das variáveis
    Vi = sld_vi.val
    theta = sld_theta.val
    m = sld_m.val
    D = sld_D.val

    # Calcular a trajetória com as novas variáveis
    x, y = calcular_trajetoria(Vi, theta, m, D)

    # Atualizar os dados do gráfico
    trajetoria.set_data(x, y)
    ax.relim()
    ax.autoscale_view()

    # Verificar o estado do checkbox
    if check_escala.get_status()[0]:
        ax.set_xlim(0, max(x))
        ax.set_ylim(0, max(y))

    # Redesenha o gráfico
    plt.draw()


# Criar a figura e os eixos
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# Calcular a trajetória inicial
x, y = calcular_trajetoria(Vi, theta, m, D)

# Plotar a trajetória inicial
(trajetoria,) = ax.plot(x, y)
plt.xlabel("Distância (m)")
plt.ylabel("Altura (m)")
plt.title("Trajetória do Projétil")

# Configurar os controles deslizantes
axcolor = "lightgoldenrodyellow"
ax_vi = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_theta = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_m = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)

sld_vi = plt.Slider(ax_vi, "Vi", 0.0, 1200.0, valinit=Vi)
sld_theta = plt.Slider(ax_theta, "Theta", 0.0, 60.0, valinit=theta)
sld_m = plt.Slider(ax_m, "m", 0.0, 15.0, valinit=m)
sld_D = plt.Slider(ax_D, "D", 0.0, 0.1, valinit=D)


# Criar o checkbox
rax = plt.axes([0.02, 0.1, 0.1, 0.1], facecolor="none", frameon=False)

check_escala = CheckButtons(
    rax,
    ["Escala Dinâmica"],
    [True],
)


sld_vi.on_changed(atualizar_grafico)
sld_theta.on_changed(atualizar_grafico)
sld_m.on_changed(atualizar_grafico)
sld_D.on_changed(atualizar_grafico)
check_escala.on_clicked(atualizar_grafico)

plt.show()
