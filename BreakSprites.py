import pygame
class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.image.load("mario.png")
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.__screen = screen
        self.__dx = 5
        self.__dy = -5
 
    def change_direction(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.__dy = -self.__dy
             
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 50) and (self.__dx < 0)) or\
           ((self.rect.right < self.__screen.get_width()-50) and (self.__dx > 0)):
            self.rect.left += self.__dx
        # If yes, then reverse the x direction. 
        else:
            self.__dx = -self.__dx
             
        # Check if we have reached the top or bottom of the court.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top > 100) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        # If yes, then reverse the y direction. 
        else:
            self.__dy = -self.__dy
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player'''
    def __init__(self,screen,image):
        '''This initializer takes a screen surface'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes for a brick paddle.
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
 
        # Otherwise, position it 10 pixels from the bottom of the screen.
        self.rect.bottom = screen.get_height()-10
 
        # Center the player horizontally in the window.
        self.rect.left = screen.get_width()/2 + 50
        self.__screen = screen
        self.__dx = 0

    
    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        y element from it, and uses this to set the players y direction.'''
        self.__dx = xy_change[1]
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the left or right of the screen.
        if ((self.rect.left > 50) and (self.__dx > 0)) or\
           ((self.rect.right < self.__screen.get_width()-50) and (self.__dx < 0)):
            self.rect.left -= (self.__dx*5)
        # If yes, then we don't change the x position of the player.
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our end zone'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and y position  as
        parameters.  '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.bottom = 480

class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "mariof", and
        sets the starting score to 0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("mariof.ttf", 20)
        self.__player_lives = 3000
        self.__player_score = 0
        self.__bricks = 108

         
    def player_scored(self, points):
        '''This method adds to the score for player and removes one from our 
        brick count'''

        self.__player_score += points
        self.__bricks -= 1
    
    def get_bricks(self):
        '''this method returns our number of bricks left on the screen'''
        return self.__bricks
           
        
    def score(self):
        '''this method checks if our player has reached the maximum score'''
        if self.__player_score == 378:
            return 1
        else:
            return 0        
    
    
    def lose_life(self):
        '''This method removes one life from player'''
        self.__player_lives-=1   
        
    def lives(self):
        '''Player loses if all 3 lives are lost.
        This method returns 0 if he has not lost yet and 1 if he has.'''
        if self.__player_lives == 0:
            return 1
        else:
            return 0
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        score = "Player Score: %d   Player Lives: %d" %(self.__player_score,self.__player_lives)
        
        self.image = self.__font.render(score, 2, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 30)
        
        

class Bricks(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''
    def __init__(self, screen, image, start_top, start_left, point):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.top = start_top
        self.rect.left = start_left
        self.points= point
    def get_points(self):
        return self.points
    
class Walls(pygame.sprite.Sprite):
    def __init__(self, screen, image, start_top, start_left):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.top = start_top
        self.rect.left = start_left
    
        

        