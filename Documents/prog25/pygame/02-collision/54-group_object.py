import pygame

pygame.init()

# tamanho da janela
window = pygame.display.set_mode((800, 600))

# define lista de retângulos que serão obstáculos
obstaculos = [
    pygame.Rect(70, 370, 100, 100),
    pygame.Rect(250, 50, 100, 100),
    pygame.Rect(450, 150, 100, 100),
    pygame.Rect(320, 20, 100, 100),
]

# definição de um player
altura = 60
largura = 40
player = pygame.Rect(0, 0, largura, altura)

# posição inicial do player
x = 5
y = 300

# velocidades do player
sentidox = 1
sentidoy = 1

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

run = True
while run:

    # código obrigatório para finalizar bem o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # pinta fundo roxo
    window.fill("purple")    

    # retorna a lista de índices dos
    # obstaculos que colidiram com o player
    indices = player.collidelistall(obstaculos)

    # vetor padrão de cores
    cores = ["blue", "blue", "blue", "blue"]

    # muda as cores dos obstaculos que colidiram
    for i in indices:
        cores[i] = "yellow"

    # desenha o player
    pygame.draw.rect(window, "green", player) 

    # desenha os obstaculos
    for i in range(len(obstaculos)):
        pygame.draw.rect(window, cores[i], obstaculos[i])

    # atualiza a tela
    pygame.display.flip()

    # o player vazou a borda da janela?
    if player.x > (800-largura) or player.x < 0:
       sentidox *= -1 # inverte o sentido 
    if player.y > (600-altura) or player.y < 0:
       sentidoy *= -1
    
    # varia a posição do círculo
    player.x += 3 * sentidox
    player.y += 3 * sentidoy

    # espera um pouco
    clock.tick(60)     

pygame.quit()