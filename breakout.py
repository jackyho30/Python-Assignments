'''Author: Jacky Ho
Date: May 5th,2017
Description: Breakout video game where user will control a mario brick paddle 
using either the arrow keys or the a and d key to move from left to right in 
order to bounce mario up towards the blocks.Paddle will continue to move in the 
direction last pressed by user. Goal is to destroy all bricks of different point
value and colour(purple=6,red=5,yellow=4,orange=3,green=2,blue=1) and achieve
max score of 378. Once half of the bricks (59) have been destroyed paddle size will 
shrink to make the game more difficult. User is given 3 lives to try and win 
the game. When the ball (mario) hits the bottom of the screen a life is lost and
mario bounces back up.

'''
# I - IMPORT AND INITIALIZE
import pygame, BreakSprites
pygame.init()
screen = pygame.display.set_mode((640, 480))
     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("breakout")
     
    # ENTITIES
    background = pygame.image.load("background.png")
    background = background.convert()
    
    # Sprites for: ScoreKeeper label, End Zones, Ball, Player and walls
    score_keeper = BreakSprites.ScoreKeeper()
    ball = BreakSprites.Ball(screen)
    player_half = BreakSprites.Player(screen,"paddle_half.png")
    player = BreakSprites.Player(screen,"paddle.png")
    player_endzone = BreakSprites.EndZone(screen)
    wall_3 = BreakSprites.Walls(screen,"wall_2.png",50,0)    
    wall_1 = BreakSprites.Walls(screen,"wall.png",0,0)
    wall_2 = BreakSprites.Walls(screen,"wall.png",0,590)

    
    #sprites for bricks
    bricks= []
    for i in range(18):
        bricks.append(BreakSprites.Bricks(screen,"purple.png",115,50+30*i,6))
        bricks.append(BreakSprites.Bricks(screen,"red.png",130,50+30*i,5))
        bricks.append(BreakSprites.Bricks(screen,"yellow.png",145,50+30*i,4))
        bricks.append(BreakSprites.Bricks(screen,"orange.png",160,50+30*i,3))
        bricks.append(BreakSprites.Bricks(screen,"green.png",175,50+30*i,2))
        bricks.append(BreakSprites.Bricks(screen,"blue.png",190,50+30*i,1))
    
    brick_group= pygame.sprite.Group(bricks)
    allSprites = pygame.sprite.OrderedUpdates(score_keeper, player_endzone, ball, player_half,player,bricks,wall_3,wall_1,wall_2)
    
    #load music and sounds
    pygame.mixer.music.load("mario_music.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)    
    coin = pygame.mixer.Sound("coin.wav")
    coin.set_volume(0.5)      

    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING: Player uses keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.change_direction((0,1))
                if event.key == pygame.K_d:
                    player.change_direction((0,-1))
                if event.key == pygame.K_LEFT:
                    player.change_direction((0,1))
                if event.key == pygame.K_RIGHT:
                    player.change_direction((0,-1))
                if event.key == pygame.K_a:
                    player_half.change_direction((0,1))
                if event.key == pygame.K_d:
                    player_half.change_direction((0,-1))
                if event.key == pygame.K_LEFT:
                    player_half.change_direction((0,1))
                if event.key == pygame.K_RIGHT:
                    player_half.change_direction((0,-1))                

        # Check if ball hits endzone
        if ball.rect.colliderect(player_endzone):
            score_keeper.lose_life()
            ball.change_direction()
 
        # Check for game over (if a player loses 3 lives)
        if score_keeper.lives()==1:
            keepGoing = False
        
        # Check for game over (if a player scores 378)
        if score_keeper.score()==1:
            keepGoing = False            
                     
        # Check if ball hits Player
        # If so, change direction
        if ball.rect.colliderect(player.rect):
            ball.change_direction()
            coin.play()
        if ball.rect.colliderect(player_half.rect):
            ball.change_direction()
            coin.play()
    
        # Multiple-Sprite Collision Detection and Reporting
        if pygame.sprite.spritecollide(ball, brick_group, False):
            ball.change_direction()        
        for index in pygame.sprite.spritecollide(ball, brick_group, True):
            score_keeper.player_scored(index.get_points())
        #removes larger paddle when half of bricks are destroyed
        if score_keeper.get_bricks()<=59:
            allSprites.remove(player)
            
        # REFRESH SCREEN
        screen.blit(background, (0, 0))
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