import pygame
import os
import random
screen_width = 600
screen_height = 600

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
skyblue = (153,204,255)
x = int(screen_width/2)
y = int(screen_height/2)
dx = 19
dy = 18
size = 40
pygame.init()
pygame.display.set_caption("공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공공")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen_width += random.randint(1,300)
    if screen_width >2400:
        screen_width = 600
    screen_height += random.randint(1,70)
    if screen_height >1200:
        screen_height = 600
    x += dx
    y += dy
    if (x + size) > screen_width or (x - size) < 0:
        dx = dx * -1
    if (y + size) > screen_height or (y - size) < 0:
        dy = dy * -1
    screen.fill(white)
    pygame.draw.circle(screen,skyblue,[x,y],size,0)
    pygame.display.flip()
    clock.tick(600)
pygame.quit()