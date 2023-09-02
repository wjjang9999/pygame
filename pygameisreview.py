import pygame
import os
import random
screen_width = 800
screen_height = 400

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
skyblue = (153,204,255)
x = 150
y = 150
dx = 0
dy = 0
x1 = 7
pygame.init()
pygame.display.set_caption("복습")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
running = True
while running:
    
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0
    if x >= screen_width-70:
        x = screen_width-70
    if y >= screen_height-60:
        y = screen_height-60
    if x <= 0:
        x = 5 
    if y <= 0:
        y = 5
    x += dx
    y += dy
    x1 += random.randint(-4,7)
    
    screen.fill(white)

    screen = pygame.display.set_mode((screen_width,screen_height))
    screen_width += 0.5
    screen.fill(white)
    pygame.draw.line(screen,red,[100,100],[200,200], 7)
    pygame.draw.line(screen,red,[200,100],[100,200], 7)
    pygame.draw.line(screen,black,[0,0],[0,800], x1)
    pygame.draw.rect(screen,green,[200,200,50,50],0)
    pygame.draw.circle(screen,black,[300,300],10,3)
    current_path = os.path.dirname(__file__)
    assets_path = os.path.join(current_path, 'assets')

    

    fish_image1 = pygame.image.load(os.path.join(assets_path, 'fish.png'))
    fish_image2 = pygame.image.load(os.path.join(assets_path, 'fish.png'))
    fish_image3 = pygame.image.load(os.path.join(assets_path, 'fish.png'))
    fish_image4 = pygame.image.load(os.path.join(assets_path, 'fish.png'))
    screen.blit(fish_image1, [random.randrange(50,131),random.randrange(50,131)])
    screen.blit(fish_image2, [random.randrange(240,311),random.randrange(70,161)])
    screen.blit(fish_image3, [random.randrange(380,461),random.randrange(100,201)])
    screen.blit(fish_image4, [x,y])
    font = pygame.font.SysFont("Malgun Gothic",30,False,False )
    font2 = pygame.font.SysFont("Malgun Gothic",20,False,False)
    text = font.render("9월2일 토요일", True, black )
    text2 = font.render("2023년", True, black )
    screen.blit(text, [10,10])
    screen.blit(text2, [10,50])
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()