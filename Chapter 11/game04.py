import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")


#load image and assign to 'sprite'
sprite = pygame.image.load('rocket.png')

#add image to game window
gamewindow.blit(sprite, (50,55))

#update the game window display
pygame.display.update()


pygame.quit()
