import pygame
import time



def main():
    g = 0.1
    HORIZONTAL_SPEED = 10

    pygame.init()


    surface = pygame.display.set_mode((800, 600))

    player_image = pygame.image.load('mario.png')
    player_image = pygame.transform.scale(player_image, (30, 30))

    running = True

    # Player Position
    PX = 60
    PY = 60

    # Action Flags
    up = False
    left = False
    right = False
    stick = False

    # Player Velocity
    PVELY = 0
    PVELX = 0

    # Ground Pos
    GY = 500

    # Ground Height
    GH = 20

    clock = pygame.time.Clock()

    while running:
        t = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True

                if event.key == pygame.K_RIGHT:
                    right = True

                if event.key == pygame.K_LSHIFT:
                    stick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    up = True

                if event.key == pygame.K_LEFT:
                    left = False

                if event.key == pygame.K_RIGHT:
                    right = False

                if event.key == pygame.K_LSHIFT:
                    stick = False

        surface.fill((0, 0, 0))

        # Drawing player and ground
        surface.blit(player_image, (PX,PY))

        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, GY, 800, GH))

        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 0, 10, 600))
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(800 - 10, 0, 10, 600))

        # Kinematics Calc
        PVELY = PVELY + g * t

        # DIY Collision
        if PY >= (GY - GH):
            PVELY = 0
            PY = GY - GH

        if PX <= 10:
            PX = 10

        if (PX <= 10) and stick:
            PVELY = 0

        if (PX <= 10) and stick and up:
            PVELY -= 40
            PX += HORIZONTAL_SPEED

        if PX >= (800 - 30):
            PX = (800 - 30)

        if (PX >= (800 - 30)) and stick:
            PVELY = 0

        if (PX >= (800 - 30)) and stick and up:
            PVELY -= 40
            PX -= HORIZONTAL_SPEED

        if (PY >= (GY - GH)) and up == True:
            PVELY -= 40

        # Movement
        if left:
            PX -= HORIZONTAL_SPEED

        if right:
            PX += HORIZONTAL_SPEED

        PY += PVELY

        # Needed
        up = False

        pygame.display.update()


if __name__ == "__main__":
    main()
