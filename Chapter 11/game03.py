import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

clock = pygame.time.Clock()

sprite = pygame.image.load('rocket.png')




pygame.quit()
