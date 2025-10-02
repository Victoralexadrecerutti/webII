# referência:
# https://www.pygame.org/docs/ref/rect.html

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

# define o retângulo que vai perceber a colisão
# xtop, ytop, largura, altura








rect = pygame.Rect(300, 200, 80, 150)


run = True
while run:

    # finalização do programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # captura de teclas
    pk = pygame.key.get_pressed()

    # se foi pressionada a tecla "q"
    if pk[pygame.K_q]:
        # sinaliza que o programa vai terminar
        run = False

    # obtém a posição do mouse
    point = pygame.mouse.get_pos()

    # verifica se houve colisão do mouse com o retângulo
    colidiu = rect.collidepoint(point)

    # coloca uma cor ou outra, dependendo se houve ou não colisão
    
    if colidiu:
        color = (255, 0, 0) 
    else:
        color = (255, 255, 255)

    # desenha informações na tela

    # fundo azul
    window.fill("blue")

    # retângulo
    pygame.draw.rect(window, color, rect)

    # atualiza a tela
    pygame.display.flip()

# finaliza o pygame
pygame.quit()
