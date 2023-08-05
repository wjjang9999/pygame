import pygame as py
import os
import random
from time import sleep
import sys

screen_width = 800
screen_height = 600

grid_size = 20
grid_width = screen_width / grid_size
grid_height = screen_height / grid_size

white = (255,255,255)
orange = (250,150,0)
gray = (100,100,100)

done = False

UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake():
    def __init__(self):
        self.create()
    def create(self):
        self.length = 2
        self.positions = [(int(screen_width / 2), int(screen_height / 2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
    def control(self,xy):
        if (xy[0] * -1,xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
    def move(self):
        cur = self.positions[0]
        x,y = self.direction
        new = (cur[0] + (x*grid_size), (cur[1]+(y*grid_size)))
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0] < 0 or new[0] >= screen_width or \
            new[1] < 0 or new[1] >= screen_height:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop

    def eat(self):
        self.length += 1
    def draw(self,screen):
        red,green,blue = 50 / (self.length - 1), 150,150 / (self.length - 1)
        for i,p in enumerate(self.positions):
            color = (100 + red * i, green,blue * i)
            rect = py.Rect((p[0],p[1]), (grid_size, grid_size))
            py.draw.rect(screen,color,rect)

class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = orange
        self.create()
    def create(self):
        x = random.randint(0,grid_width - 1)
        y = random.randint(0,grid_height - 1)
        self.position = x * grid_size, y * grid_size
    def draw(self,screen):
        rect = py.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        py.draw.rect(screen,self.color,rect)
class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5
    def process_events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                return True
            elif event.type == py.KEYDOWN:
                if event.key == py.K_UP:
                    self.snake.control(UP)
                elif event.key == py.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == py.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == py.K_RIGHT:
                    self.snake.control(RIGHT)
        return False
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.speed = (10 + self.snake.length) / 2
    def check_eat(snake,feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    def draw_info(self,length,speed,screen):
        info = "Length: " + str(length) + "    " + "Speed: " + str(round(speed, 2))
        font = py.font.SysFont('FixedSys', 30, False, False)
        text_obj = font.render(info,True,gray)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10,10
        screen.blit(text_obj,text_rect)
    def display_frame(self,screen):
        screen.fill(white)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen,(0,0))

    
def main():
    py.init()
    py.display.set_caption("snake game")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()
game = Game()
def __name__():
    main()
while not done:
    done = game.process_events()
    game.run_logic()
    game.display_frame(screen)
    py.display.flip()
    clock.tick(120)
if __name__ == '__main__':
    main()