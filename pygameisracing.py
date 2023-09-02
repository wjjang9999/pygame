import pygame
import os
import random
import time
import sys
screen_width = 480
screen_height = 800

black = (0,0,0)
white = (255,255,255)
gray = (150,150,150)
red = (255,0,0)

car_count = 3
lane_count = 5 
speed = 10

class Lane():
    def __init__(self):
        self.color = white
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (screen_width - (self.width * lane_count)) / (lane_count - 1)
        self.count = 10
        self.x = 0
        self.y = -self.height
    
    def move(self, speed, screen):
        self.y += speed
        if self.y > 0:
            self.y = -self.height
        self.draw(screen)
    def draw(self, screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.width, self.height))
            next_lane += self.height + self.gap
class Car():
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        car_images_path = resource_path('assets/car')
        image_file_list = os.listdir(car_images_path)
        self.image_path_list = [os.path.join(car_images_path,file)for file in image_file_list if file.endswith(".png")]

        crash_image_path = resource_path('assets/crash.png')
        self.crash_image = pygame.image.load(crash_image_path)

        crash_sound_path = resource_path('assets/crash.wav')
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)

        collision_sound_path = resource_path('assets/collision.wav')
        self.collision_sound = pygame.mixer.Sound(collision_sound_path)

        engine_sound_path = resource_path('assets/engine.wav')
        self.engine_sound = pygame.mixer.Sound(engine_sound_path)
    def load_image(self):
        choice_car = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
    
    def load(self):
        self.load_image()
        self.x = screen_width // 2
        self.y = screen_height - self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()
    def load_random(self):
        self.load_image
        


def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)
def main():
    pygame.init()
    pygame.display.set_caption("수동차 게임")
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(gray)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()