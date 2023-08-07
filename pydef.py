import pygame
import time
import random
def pyrects():
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
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        screen.fill(white)
        pygame.draw.rect(screen,black,[50,50,100,100],0)
        rect2 = pygame.Rect(0,0,50,50)
        rect2.center = (screen_width//2,screen_height//2)
        pygame.draw.rect(screen,blue,rect2,0)
        rect3 = pygame.Rect(200,200,20,20)
        rect4 = (200,200,40,40)
        rect5 = (180,180,60,60)
        pygame.draw.rect(screen,red,rect5,0)
        pygame.draw.rect(screen,green,rect4,0)
        pygame.draw.rect(screen,red,rect3,0)
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
def pyrectchange():
    screen_width = 800
    screen_height = 600
    white = (255,255,255)
    black = (0,0,0)
    blue = (0,0,255)
    red = (255,0,0)
    green = (0,255,0)
    running = True
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    color = black
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

def pynotscreenexit():
    screen_width = 800
    screen_height = 800
    
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    running = True
    white = (255,255,255)
    black = (0,0,0)
    rect_x = screen_width/2
    rect_y = screen_height/2
    rect_dx = 0
    rect_dy = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rect_dx = 5
                elif event.key == pygame.K_LEFT:
                    rect_dx = -5
                elif event.key == pygame.K_UP:
                    rect_dy = -5
                elif event.key == pygame.K_DOWN:
                    rect_dy = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    rect_dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    rect_dy = 0
        rect_x += rect_dx
        rect_y += rect_dy
        
        if (rect_x + 20) > screen_width:
            rect_x = rect_x - 5
        if (rect_y + 20) > screen_height:
            rect_y = rect_y - 5
        if rect_x < 0:
            rect_x = rect_x + 5
        if rect_y < 0:
            rect_y = rect_y + 5
        screen.fill(white)
        
        pygame.draw.rect(screen,black,[rect_x,rect_y,20,20],0)
        pygame.display.flip()
        clock.tick(60)
    
    
    
    pygame.quit()