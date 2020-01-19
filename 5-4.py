# I - Import and Initialize
import pygame
pygame.init()
 
def status_surface(draw_color, line_width):
    """ creates a Surface object for status text """
    my_font = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (draw_color, line_width)
    status = my_font.render(status_string, 1, (draw_color))
    return status
 
def main():
    '''This function defines the 'mainline logic' for our paint program.'''
     
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint:  (w)hite, blac(k), (c)lear, (q)uit")
     
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    load = False     
    # A - Action (broken into ALTER steps)
     
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    line_start = (0, 0)
    draw_color = (0, 0, 0)
    line_width = 3
    
    # L - Loop
    while keepGoing:
    
        # T - Timer to set frame rate
        clock.tick(30)
     
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                line_end = pygame.mouse.get_pos()
        # Check if left mouse button is down
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if not load:
                        pygame.draw.line(background, draw_color, line_start, line_end, line_width)
                    if load:
                        pygame.draw.line(image, draw_color, line_start, line_end, line_width)
                line_start= line_end
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    #quit    
                    keepGoing = False
                elif event.key == pygame.K_c:
                    #clear screen
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    #white
                    draw_color = (255, 255, 255)
                elif event.key == pygame.K_k:
                    #black
                    draw_color = (0, 0, 0)
               
                elif event.key == pygame.K_r:
                    draw_color = (255,0,0)
                elif event.key == pygame.K_g:
                    draw_color = (0,255,0)             
                elif event.key == pygame.K_b:
                    draw_color = (0,0,255)  
                    
                elif event.key == pygame.K_1:
                    line_width=1 
                elif event.key == pygame.K_2:
                    line_width=2
                elif event.key == pygame.K_3:
                    line_width=3
                elif event.key == pygame.K_4:
                    line_width=4
                elif event.key == pygame.K_5:
                    line_width=5
                elif event.key == pygame.K_6:
                    line_width=6
                elif event.key == pygame.K_7:
                    line_width=7
                elif event.key == pygame.K_8:
                    line_width=8
                elif event.key == pygame.K_9:
                    line_width=9  
                
                elif event.key == pygame.K_s:
                    if load:
                        pygame.image.save(image,"painting.bmp")
                    if not load:
                        pygame.image.save(background,"painting.bmp")
                elif event.key == pygame.K_l:
                    load = True
                    image = pygame.image.load("painting.bmp")
                    image = image.convert()
                    
                    
                    
                    
        # R - Refresh display
        if not load:
            screen.blit(background, (0, 0))
        if load:
            screen.blit(image, (0,0))
            screen.blit(my_label, (0, 450))
        if not load:
            my_label = status_surface(draw_color, line_width)
            screen.blit(my_label, (0, 450))
        pygame.display.flip()
        
        
    # Close the game window
    pygame.quit()    
    
        
# Call the main function
main()