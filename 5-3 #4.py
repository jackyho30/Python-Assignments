# I - Import and Initialize
import pygame, math
pygame.init()

def main():
    # D - Display configuration
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("5-2 # 4")
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    
    face = pygame.image.load("portrait.png")
    face = face.convert()  
    
    mySystemFont = pygame.font.SysFont("Arial", 60)
    label = mySystemFont.render("Jimmy", 1, (0, 0, 0))    
    
    
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
        screen.blit(face, (0, 0))
        screen.blit(label, (0, 100))
        pygame.display.flip()
    # Save the background surface as a PNG file
    pygame.image.save(screen,"new-portrait.bmp")
    # Close the game window
    pygame.quit()
    
main()