# I - Import and Initialize
import pygame
pygame.init()

# D - Display configuration
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("5-1")

# E - Entities (just background for now)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

#box 1 moving right, red
box_1 = pygame.Surface((25, 25))
box_1 = box_1.convert()
box_1.fill((255, 0, 0))
#box 2 moving down, green
box_2 = pygame.Surface((25, 25))
box_2 = box_2.convert()
box_2.fill((0, 255, 0))
#box 3 moving diagonally from top left, blue 
box_3 = pygame.Surface((25, 25))
box_3 = box_3.convert()
box_3.fill((0, 0, 255))
#box 4 moving diagonally from top right, yellow
box_4 = pygame.Surface((25, 25))
box_4 = box_4.convert()
box_4.fill((255, 255, 0))

box_1_x= 0
box_1_y= 240

box_2_x= 320
box_2_y= 0 

box_3_x= 0
box_3_y= 0

box_4_x= 640
box_4_y= 0


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
    #makes the boxes move
    box_1_x+= 10
    box_2_y+= 10
    box_3_x+= 10
    box_3_y+= 10
    box_4_x-= 10
    box_4_y+= 10
    # causes boxes to reset when reaching end of screen
    if box_1_x> screen.get_width():
        box_1_x = 0
    if box_2_y> screen.get_height():
        box_2_y = 0  
    if box_3_y> screen.get_height():
        box_3_y = 0  
    if box_3_x> screen.get_width():
        box_3_x = 0      
    if box_4_y> screen.get_height():
        box_4_y = 0  
    if box_4_x< 0:
        box_4_x = 640        
    # R - Refresh display
    screen.blit(background, (0, 0))
    screen.blit(box_1, (box_1_x, box_1_y))
    screen.blit(box_2, (box_2_x, box_2_y))
    screen.blit(box_3, (box_3_x, box_3_y))
    screen.blit(box_4, (box_4_x, box_4_y))
    pygame.display.flip()

# Close the game window
pygame.quit()