import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

sprite = pygame.image.load('rocket.png')


#initialize our variables
running = 1
x=250
y=280


while running: 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10 #shift image left 10 pixels
            elif event.key == pygame.K_RIGHT:
                x = x + 10 #shift image right 10 pixels
        if event.type == pygame.QUIT:  
            running = 0 #close

    gamewindow.blit(sprite, (x,y))
    pygame.display.update()
    gamewindow.fill((0,0,0)) #clear screen 

pygame.quit()
