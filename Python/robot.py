# pgzero
import random

WIDTH = 600  # Largura da janela
HEIGHT = 300  # Altura da janela

TITLE = "CAPTCHA"  # Título da janela do jogo
FPS = 30  # Taxa de quadros

# Variáveis com gráficos
fon = Actor('back')
coddy = Actor('avatar', (50, 240))
fireball = Actor('dron_2', (700, 240))
fireball_2 = Actor('dron', (1000, 170))
go = Actor('go1')
win = Actor('win1')
game_over = 0
count = 0
# Variável aleatória
enemy = random.randint(1, 2)
# Velocidade
speed = 5

# Renderização


def draw():
    fon.draw()
    coddy.draw()
    # Obstáculo aleatório
    if enemy == 1:
        fireball.draw()
    else:
        fireball_2.draw()

    screen.draw.text(count, pos=(10, 10), color="white", fontsize=24)

    if game_over == 1:
        go.draw()
    if count == 10:
        win.draw()
        screen.draw.text("Você aprenderá a criar jogos como esse neste curso!", pos=(
            50, 200), color="white", fontsize=20)


# A função de atualização
def update(dt):
    global game_over
    global count
    global enemy
    global speed
    global win

    # Obstáculo aleatório
    if enemy == 1:
        if fireball.x > -20:
            fireball.x = fireball.x - speed
        else:
            fireball.x = WIDTH + 20
            # Aumentando a variável ⬇
            count += 1
            enemy = random.randint(1, 2)
            speed += 1

    # Segunda variável
    else:
        if fireball_2.x > -20:
            fireball_2.x = fireball_2.x - speed
        else:
            fireball_2.x = WIDTH + 20
            # Aumentando a variável ⬇
            count += 1
            enemy = random.randint(1, 2)
            speed += 1

    # Controles
    if keyboard.left and coddy.x > 20:
        coddy.x = coddy.x - 5
    elif keyboard.right and coddy.x < 580:
        coddy.x = coddy.x + 5

    # Reiniciando
    if game_over == 1 and keyboard.enter:
        game_over = 0
        coddy.pos = (50, 240)
        fireball.pos = (700, 240)
        fireball_2.pos = (1000, 150)
        count = 0
        speed = 5

    # Colisão
    if coddy.colliderect(fireball) or coddy.colliderect(fireball_2):
        game_over = 1

# Animações


def on_key_down(key):
    # Pular
    if keyboard.up:
        coddy.y = 100
        animate(coddy, tween='bounce_end', duration=2, y=240)

    # Esquivar
    elif keyboard.down:
        coddy.y = 245
        animate(coddy, duration=1, y=240)
