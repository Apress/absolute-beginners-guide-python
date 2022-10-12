import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#load image and assign to 'sprite'
sprite = pygame.image.load('rocket.png')

running = 1
x=250
y=280

while running: 
    #add image to game window
    gamewindow.blit(sprite, (x,y))

    #update the game window display
    pygame.display.update()


pygame.quit()
