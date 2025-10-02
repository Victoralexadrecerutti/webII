import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color


    # desenha um círculo
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    # circle(surface, color, center, radius, width)
    # superfície, cor, centro, raio, borda    
    pygame.draw.circle(screen, (10, 10, 10), [320, 320], 15, 5)
    
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    

