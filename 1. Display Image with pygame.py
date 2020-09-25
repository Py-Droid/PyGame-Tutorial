"""Display Image With Pygame"""

import pygame

pygame.init()

display_width = 800
display_height = 600
gameDisply= pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Race Game")

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("img/image.jpeg")
crashed = False

def car(x, y):
    gameDisply.blit(carImg, (x, y))

x = display_width * 0.45
y = display_height * 0.8

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    gameDisply.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()