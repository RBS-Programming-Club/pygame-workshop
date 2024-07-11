import pygame

pygame.init()

# (width, height)
window = pygame.display.set_mode((640,480))

running = True

player_image = pygame.image.load('mario.png')

# Resizing image (player_image, (width, height))
player_image = pygame.transform.scale(player_image, (200,200))

playerX = 0
playerY = 0

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX = playerX - 10
            if event.key == pygame.K_RIGHT:
                playerX = playerX + 10

    # Background Color (R, G, B)
    window.fill((82, 154, 254))
    
    # Drawing Mario! ([player image], (x,y))
    window.blit(player_image, (playerX,playerY))

    pygame.display.update()