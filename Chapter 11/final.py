import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#load rocket image
sprite = pygame.image.load('rocket.png') 

#initialise running state to 1 for game loop
running = 1

# set initial position for image
x = 250
y = 280

#turn on key repeat
pygame.key.set_repeat(1, 25)


#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = 0 #close
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10 #shift image left 10 pixels
            elif event.key == pygame.K_RIGHT:
                x = x + 10 #shift image right 10 pixels

    gamewindow.fill((0,0,0)) #clear screen   
    gamewindow.blit(sprite, (x,y)) #redraw sprite in new position
    pygame.display.update() #update screen


pygame.quit()
