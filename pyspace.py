import pygame
screen_width = 800
screen_height = 600
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
done = False
pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
color = black
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                color = red
        elif event.type == pygame.KEYUP:
            color = black
    screen.fill(white)
    rect = pygame.Rect(400,300,100,100)
    pygame.draw.rect(screen,color,rect,0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()