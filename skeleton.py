# Demo #1: Skeleton IDEA/ALTER Framework

# I - Import and Initialize
import pygame
pygame.init()

# D - Display configuration
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello, world!")

# E - Entities (just background for now)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 255))

# A - Action (broken into ALTER steps)

    # A - Assign values to key variables
clock = pygame.time.Clock()
keepGoing = True

    # L - Loop
while keepGoing:

    # T - Timer to set frame rate
    clock.tick(30)

    # E - Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    # R - Refresh display
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Close the game window
pygame.quit()