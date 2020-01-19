'''g,h,a,d,f'''
# I - IMPORT AND INITIALIZE
import pygame, pySprites
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
# Create a list of Joystick objects.
joysticks = []
for joystick_no in range(pygame.joystick.get_count()):
    stick = pygame.joystick.Joystick(joystick_no)
    stick.init()
    joysticks.append(stick)
     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("pyPong! v1.0")
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
 
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Players
    score_keeper = pySprites.ScoreKeeper()
    ball = pySprites.Ball(screen)
    player1 = pySprites.Player(screen, 1)
    player1_endzone = pySprites.EndZone(screen,0)
    player2 = pySprites.Player(screen, 2)
    player2_endzone = pySprites.EndZone(screen,639)
    allSprites = pygame.sprite.Group(score_keeper, player1_endzone, \
                                     player2_endzone, ball, player1, player2)
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.JOYHATMOTION:
                player1.change_direction(event.value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2.change_direction((0, 1))
                if event.key == pygame.K_DOWN:
                    player2.change_direction((0, -1))
 
        # Check if player 1 scores (i.e., ball hits player 2 endzone)
        if ball.rect.colliderect(player2_endzone):
            score_keeper.player1_scored()
            ball.change_direction()
 
        # Check if player 2 scores (i.e., ball hits player 1 endzone)
        if ball.rect.colliderect(player1_endzone):
            score_keeper.player2_scored()
            ball.change_direction()
             
        # Check for game over (if a player gets 3 points)
        if score_keeper.winner():
            keepGoing = False
                     
        # Check if ball hits Player 1 or 2
        # If so, change direction, and speed up the ball a little
        if ball.rect.colliderect(player1.rect) or\
           ball.rect.colliderect(player2.rect):
            ball.change_direction()
                     
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()     
     
# Call the main function
main()        