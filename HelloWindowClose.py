import pygame

pygame.init()

# (width, height)
window = pygame.display.set_mode((640,480))

# Window Name
pygame.display.set_caption("Mario Game")

running: bool = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background Color (R, G, B)
    window.fill((82,154,254))

    # Updates the screen
    pygame.display.update()