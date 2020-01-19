# I - Import and Initialize
import pygame, math
pygame.init()

def drawStuff(background):
    #head
    pygame.draw.circle(background, (255,218,185), (240,240), 100, 0)
    #left eye
    pygame.draw.circle(background, (255, 255, 255), (200, 210), 10, 0)
    #left pupil
    pygame.draw.circle(background, (0,0,0), (200,210), 5, 0)
    #right eye
    pygame.draw.circle(background, (255, 255, 255), (280, 210), 10, 0)
    #right pupil
    pygame.draw.circle(background, (0,0,0), (280,210), 5, 0)
    #mouth
    pygame.draw.line(background, (0,0,0), (220, 280), (260, 280))
    #hat
    pygame.draw.arc(background, (0, 0, 0), ((140, 100), (200, 200)), 0, math.pi, 0)
    pygame.draw.arc(background, (0,0,0), (50,50,200,300), 20, 20)

    
    
def main():
    # D - Display configuration
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("5-3 # 4")
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    

    
    drawStuff(background)
    
    
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
    pygame.image.save(background, "portrait.png")
    
    # Close the game window
    pygame.quit()
    
main()