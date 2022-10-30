import pygame
import math
import random

pygame.init()

gamewindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game Window")

#load rocket image
sprite = pygame.image.load('rocket.png')

#load ufo image
ufo = pygame.image.load('ufo.png')

#load bullet image
bulletImage = pygame.image.load('bullet.png')

#load explosion image
exp = pygame.image.load('explosion.png')

#initialise running state to 1 for game loop
running = 1

#set horizontal and vertical offset ufo moves 5 pixels at a time
speed = [5, 5]

# set initial position for rocket image
x = 250
y = 400

#ufo direction
ufo_X_dir = 0
ufo_Y_dir = 0

#ufo position
ufo_X_pos = 0
ufo_Y_pos = 0

#initialise bullets
bullet_X = 0
bullet_Y = y
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "nofire"

#create our game clock
clock = pygame.time.Clock()

#turn on key repeat
pygame.key.set_repeat(1, 25)

#assign image to rectangle so we can manipulate its position
ufo_rect = ufo.get_rect()

#chech for a collision between bullet and ufo
def isCollision(ufo_X_pos, ufo_Y_pos, bullet_X, bullet_Y):
   distance = math.sqrt(math.pow(ufo_X_pos - bullet_X, 2) + (math.pow(ufo_Y_pos - bullet_Y, 2)))
   if distance < 35:
      return True
   else:
      return False

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
        ufo_X_dir=ufo_X_dir-1

    #if ufo goes off right edge reverse x direction
    if ufo_rect.right > 800:
        speed[0] = -speed[0]
        ufo_X_dir=ufo_X_dir+1
        
    #if ufo goes off top edge reverse y direction
    if ufo_rect.top < 0:
        speed[1] = -speed[1]
        ufo_Y_dir=ufo_Y_dir-1

    #if ufo goes off bottom edge reverse y direction
    if ufo_rect.bottom > 600:
        speed[1] = -speed[1]
        ufo_Y_dir=ufo_Y_dir+1

    #set position of UFO (center of the ufo rectangle
    ufo_X_pos = ufo_rect.centerx
    ufo_Y_pos = ufo_rect.centery

    #clear screen for next frame
    gamewindow.fill((0,0,0)) 

    # Collision
    collision = isCollision(ufo_X_pos, ufo_Y_pos, bullet_X, bullet_Y)
    if collision:
         bullet_Y = 380
         bullet_state = "nofire"
         gamewindow.blit(exp, (ufo_X_pos, ufo_Y_pos)) #show explosion image
         #place ufo back on screen in random position
         ufo_rect.left = random.randint(0, 736) 
         ufo_rect.left = random.randint(50, 150)

    #keypress event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = 0 #close
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10 #shift image left 10 pixels
            elif event.key == pygame.K_RIGHT:
                x = x + 10 #shift image right 10 pixels
            elif event.key == pygame.K_SPACE:  # file bullet
                if bullet_state == "nofire":
                    bullet_X = x + 30 #move bullet to rocket position
                    gamewindow.blit(bulletImage, (bullet_X, bullet_Y))
                    bullet_state = "fire"


    # move bullet after user presses space
    if bullet_Y <= 0:
        bullet_Y = y
        bullet_state = "nofire"
    if bullet_state == "fire":
        gamewindow.blit(bulletImage, (bullet_X, bullet_Y))
        bullet_state = "fire"
        bullet_Y -= bullet_Ychange


    gamewindow.blit(ufo,ufo_rect) #redraw ufo in new position
    gamewindow.blit(sprite, (x,y)) #redraw rocket sprite in new position
    pygame.display.update() #update screen


pygame.quit()
