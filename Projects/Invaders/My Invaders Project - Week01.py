import pygame

class Ship():
    def __init__(self, screen):
        #Initialize the ship, and set its starting position.
        self.screen = screen

        # Load the rocket image
        self.image = pygame.image.load('rocket.png')

        # Creates a surface and adds the rocket image.
        #Aan object which specifically stores coordinates
        # (x and y) and dimensions (width, and height)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def draw(self):
        #Draw the ship at current location
        #self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.rect)


        

# Initialize game and create a screen object.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Invaders")

# Make a ship object.
ship = Ship(screen)

# Set the background color.
background = pygame.image.load("bg.jpg")

#create our game clock
clock = pygame.time.Clock()

#turn on key repeat
pygame.key.set_repeat(1, 25)

#initialise running state to 1 for game loop
running = 1




# Start  game loop.
while running:

    #execute loop at 25 frames per second
    clock.tick(25)

    # Clear screen a - add background image.
    screen.blit(background, (0, 0))
        
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right.
                ship.rect.centerx += 10
            if event.key == pygame.K_LEFT:
                #Move the ship to the left.
                ship.rect.centerx -= 10



    # draw the ship
    ship.draw()

    

    # update screen.
    pygame.display.update()
        

pygame.quit()

