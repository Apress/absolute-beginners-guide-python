import pygame
import random

class Rocket():
    def __init__(self, screen):
        #Initialize rocket, and set starting position.
        self.screen = screen

        # Load the rocket image
        self.image = pygame.image.load('rocket.png')

        # Creates a surface and adds the rocket image.
        #Aan object which specifically stores coordinates
        # (x and y) and dimensions (width, and height)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set rocket to the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def draw(self):
        #Draw the rocket at current location
        self.screen.blit(self.image, self.rect)




class UFO():
    def __init__(self, screen):
        # Initialize the alien, and set its starting position.
        super(UFO, self).__init__()
        self.screen = screen
        
        self.speed = [5, 5]

        #ufo direction
        self.ufo_X_dir = 0
        self.ufo_Y_dir = 0

        #ufo position
        self.ufo_X_pos = 0
        self.ufo_Y_pos = 0

        # Load the ufo image, and set its rect attribute.
        self.image = pygame.image.load('ufo.png')
        self.rect = self.image.get_rect()

        # Start each new ufo at random position
        self.rect.x = random.randint(100,600)
        self.rect.y = random.randint(100,600)

        # Store the ufo's exact position.
        self.x = float(self.rect.x)
        

    def draw(self):
        # Draw the ufo at its current location.
        self.screen.blit(self.image, self.rect)


    def move(self):
        # move ufo by given offset (x,y)
        self.rect.move_ip(self.speed) #ufo_rect.move_ip (x, y)

        #bounce the ufo off the 4 edges
        #if ufo goes off left edge x reverse direction
        if self.rect.left < 0:
            self.speed[0] = -self.speed[0]
            self.ufo_X_dir=self.ufo_X_dir-1

        #if ufo goes off right edge reverse x direction
        if self.rect.right > 800:
            self.speed[0] = -self.speed[0]
            self.ufo_X_dir=self.ufo_X_dir+1
        
        #if ufo goes off top edge reverse y direction
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            self.ufo_Y_dir=self.ufo_Y_dir-1

        #if ufo goes off bottom edge reverse y direction
        if self.rect.bottom > 600:
            self.speed[1] = -self.speed[1]
            self.ufo_Y_dir=self.ufo_Y_dir+1
    
        #set position of UFO (center of the ufo rectangle
        self.ufo_X_pos = self.rect.centerx
        self.ufo_Y_pos = self.rect.centery




# main program


# Initialize game and create a screen object.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Invaders")

# Make a rocket object.
rocket = Rocket(screen)

# create a UFO
ufo = UFO(screen)

# create anther UFO
ufo2 = UFO(screen)

# Set the background color.
background = pygame.image.load("bg.jpg")

#create our game clock
clock = pygame.time.Clock()

#turn on key repeat
pygame.key.set_repeat(1, 25)

#initialise running state to 1 for game loop
running = 1


# Game loop.
while running:

    #execute loop at 25 frames per second
    clock.tick(25)

    # Clear screen a - add background image.
    screen.blit(background, (0, 0))

        
    # Keyboard event handler.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the rocket to the right.
                rocket.rect.centerx += 10
            if event.key == pygame.K_LEFT:
                #Move the rocket to the left.
                rocket.rect.centerx -= 10



    # draw the rocket
    rocket.draw()

    # draw the ufos
    ufo.draw()
    ufo2.draw()

    # move the ufos
    ufo.move()
    ufo2.move()

    # update screen.
    pygame.display.update()
        

pygame.quit()

