import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#initialise game clock
clock = pygame.time.Clock()

#initialise running state to 1 for game loop
running = 1


#set horizontal by vertical list
speed = [10, 0]


#load ufo image
ufo = pygame.image.load('ufo.png')

#assign image to rectangle so we can manipulate its position
ufo_rect = ufo.get_rect()


#game loop
while running:

    #execute loop at 25 frames per second
    clock.tick(25)
    

    # move ufo
    ufo_rect.move_ip(speed)
    

    gamewindow.fill((0,0,0)) #clear screen

    gamewindow.blit(ufo,ufo_rect) #redraw ufo in new position

    pygame.display.update() #update screen


pygame.quit()
