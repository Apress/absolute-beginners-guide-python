import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#initialise running state to 1 for game loop
running = 1


#set horizontal by vertical
speed = [1, 0]


#load ufo image
ufo = pygame.image.load('ufo.png')

#assign image onto rectangle so we can manipulate it
ufo_rect = ufo.get_rect()


#game loop
while running:


    # move ufo
    ufo_rect.move_ip(speed)

    
    gamewindow.fill((0,0,0)) #clear screen

    gamewindow.blit(ufo,ufo_rect) #redraw ufo in new position

    pygame.display.update() #update screen


pygame.quit()
