import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#load rocket image
sprite = pygame.image.load('rocket.png')

#load ufo image
ufo = pygame.image.load('ufo.png')

#load bullet image
bulletImage = pygame.image.load('bullet.png')

#initialise running state to 1 for game loop
running = 1

#set horizontal and vertical offset
speed = [10, 10]

# set initial position for image
x = 250
y = 280


#initialise bullets
bullet_X = 0
bullet_Y = 280
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "nofire"

#create our game clock
clock = pygame.time.Clock()


#turn on key repeat
pygame.key.set_repeat(1, 25)

#assign image to rectangle so we can manipulate its position
ufo_rect = ufo.get_rect()

#game loop
while running:
    #execute loop at 25 frames per second
    clock.tick(25)

    # move ufo by given offset (x,y)
    ufo_rect.move_ip(speed) #ufo_rect.move_ip (x, y)


    #bounce the ufo off the 4 edges
    #if ufo goes off left edge x reverse direction
    if ufo_rect.left < 0:
        speed[0] = -speed[0] 

    #if ufo goes off right edge reverse x direction
    if ufo_rect.right > 640:
        speed[0] = -speed[0]
        
    #if ufo goes off top edge reverse y direction
    if ufo_rect.top < 0:
        speed[1] = -speed[1] 

    #if ufo goes off bottom edge reverse y direction
    if ufo_rect.bottom > 480:
        speed[1] = -speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = 0 #close
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10 #shift image left 10 pixels
            elif event.key == pygame.K_RIGHT:
                x = x + 10 #shift image right 10 pixels
            elif event.key == pygame.K_SPACE:  # file bullet
                if bullet_state is "nofire":
                    bullet_X = x + 30
                    gamewindow.blit(bulletImage, (bullet_X, bullet_Y))
                    bullet_state = "fire"

    gamewindow.fill((0,0,0)) #clear screen

    # move bullet after user presses space
    if bullet_Y <= 0:
        bullet_Y = 280
        bullet_state = "nofire"
    if bullet_state is "fire":
        gamewindow.blit(bulletImage, (bullet_X, bullet_Y))
        bullet_state = "fire"
        bullet_Y -= bullet_Ychange

    gamewindow.blit(ufo,ufo_rect) #redraw ufo in new position
    gamewindow.blit(sprite, (x,y)) #redraw sprite in new position
    pygame.display.update() #update screen


pygame.quit()
