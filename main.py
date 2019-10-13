import pygame
from circle import Circle

size = width, height = 400, 300
main_screen = pygame.display.set_mode(size)
static_screen = pygame.Surface(main_screen.get_size())
static_screen.fill(pygame.Color('black'))

running = True

circles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            circles += [Circle(x1, y1, 300)]

    # Рисуем на экране сохраненное на втором холсте
    main_screen.fill(pygame.Color('black'))

    for i in range(len(circles) - 1, -1, -1):
        if circles[i].y == circles[i].bound_y:
            circles[i].draw(static_screen)
            del circles[i]

    main_screen.blit(static_screen, (0, 0))

    for c in circles:
        c.draw(main_screen)

    pygame.display.flip()

pygame.quit()