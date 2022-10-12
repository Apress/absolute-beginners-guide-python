import pygame

pygame.init()

gamewindow = pygame.display.set_mode((640,480))
pygame.display.set_caption("Game Window")

running=1

#define colours using RGB values
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red   = (255, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = 0 #close


    #draw a circle
    pygame.draw.circle(gamewindow, green, (200, 100), 43, 0)

    #draw an ellipse
    pygame.draw.ellipse(gamewindow, blue, (400, 66, 60, 77), 6)

    #draw a rectangle
    pygame.draw.rect(gamewindow, red, (300, 200, 100, 150))

    

    pygame.display.update() #update screen


pygame.quit()
