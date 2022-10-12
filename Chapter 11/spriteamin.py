import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

#create our game clock
clock = pygame.time.Clock()

#turn on key repeat
pygame.key.set_repeat(1, 25)

counter=0
running=1
x=55
y=55


#load animation frames into list
frames = [pygame.image.load('frame1.png'),
          pygame.image.load('frame2.png'),
          pygame.image.load('frame3.png')]


#game loop
while running:
    #execute loop at 25 frames per second
    clock.tick(25)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = 0 #close
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 10 #shift image right 10 pixels
            elif event.key == pygame.K_RIGHT:
                x = x + 10 #shift image right 10 pixels

    gamewindow.fill((0,0,0)) #clear screen

    
    gamewindow.blit(frames[counter], (x,y)) #redraw sprite in new position
    counter = (counter + 1) % len(frames) #move to next frame in frames list
    

    pygame.display.update() #update screen


pygame.quit()
