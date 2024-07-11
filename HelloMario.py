import pygame

pygame.init()

# (width, height)
window = pygame.display.set_mode((640,480))

running = True

player_image = pygame.image.load('mario.png')

# player_image = pygame.transform.scale(player_image, (200,200))

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background Color (R, G, B)
    window.fill((82, 154, 254))

    # Drawing Mario! ([player image], (x,y))
    window.blit(player_image, (100,100))

    # Updates the screen
    pygame.display.update()