import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#initialise game clock
clock = pygame.time.Clock()

#initialise running state to 1 for game loop
running = 1

#set horizontal and vertical offset
speed = [10, 10]

#load ufo image
ufo = pygame.image.load('ufo.png')

#assign image to rectangle so we can manipulate its position
ufo_rect = ufo.get_rect()


#game loop
while running:

    #execute loop at 30 frames per second
    clock.tick(30)

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

    
    gamewindow.fill((0,0,0)) #clear screen

    gamewindow.blit(ufo,ufo_rect) #redraw ufo in new position

    pygame.display.update() #update screen


pygame.quit()
