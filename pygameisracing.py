import pygame
import os
import sys
import random
from time import sleep

SCREEN_WIDTH = 2500
SCREEN_HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (200, 0, 0)

CAR_COUNT = 30
LANE_COUNT = 12
SPEED = 11
FPS = 70


def random_djrRk():
        djrRka = random.randrange(1,10000)
        return djrRka
class Car():
    
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        car_images_path = resource_path('assets/car')
        image_file_list = os.listdir(car_images_path)
        self.image_path_list = [os.path.join(car_images_path, file)
                                for file in image_file_list if file.endswith(".png")]
        crash_image_path = resource_path('assets/crash.png')
        crash_sound_path = resource_path('assets/crash.wav')
        collision_sound_path = resource_path('assets/collision.wav')
        engine_sound_path = resource_path('assets/engine.wav')
        self.crash_image = pygame.image.load(crash_image_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
        self.collision_sound = pygame.mixer.Sound(collision_sound_path)
        self.engine_sound = pygame.mixer.Sound(engine_sound_path)

    def load_image(self):
        choice_car_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car_path)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def load(self):
        self.load_image()
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()

    def load_random(self):
        self.load_image()
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        if random_djrRk() == 1:
            self.dy = random.randint(5,9)
            self.dx = 0
        elif random_djrRk() >= 2 or random_djrRk() <= 9000:
            self.dy = random.randint(5,17)
            self.dx = 0
        else:
            self.dy = random.randint(5,19)
            self.dx = random.randint(-3,3)
            
            


    def move(self):
        self.x += self.dx
        self.y += self.dy

    def out_of_screen(self):
        if self.x + self.width > SCREEN_WIDTH or self.x < 0:
            self.x -= self.dx
        if self.y + self.height > SCREEN_HEIGHT or self.y < 0:
            self.y -= self.dy

    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) \
           and (self.y < car.y + car.height) and (self.y + self.height > car.y):
            return True
        else:
            return False

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def draw_crash(self, screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x + int(self.width / 2) - int(width / 2)
        draw_y = self.y + int(self.height / 2) - int(height / 2)
        screen.blit(self.crash_image, [draw_x, draw_y])
        pygame.display.update()

class Lane():
    def __init__(self):
        self.color = WHITE
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (SCREEN_WIDTH - (self.width * LANE_COUNT)) / (LANE_COUNT - 1)
        self.count = 11
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
            pygame.draw.rect(screen, self.color, [self.x, next_lane, self.width, self.height])
            next_lane += self.height + self.gap

class Game():
    def __init__(self):
        menu_image_path = resource_path('assets/menu_car.png')
        djrRK_image_path = resource_path('assets/억까가 매우 많을 수 있으니 주의 하시길 바랍니다.png')
        self.image_intro = pygame.image.load(menu_image_path)
        self.djrRK_image = pygame.image.load(djrRK_image_path)
        self.djrRK_image = pygame.transform.rotate(self.djrRK_image, 330)
        pygame.mixer.music.load(resource_path('assets/race.wav'))
        font_path = resource_path('assets/NanumGothicCoding-Bold.ttf')
        self.font_40 = pygame.font.Font(font_path, 40)
        self.font_30 = pygame.font.Font(font_path, 30)
        self.font_90 = pygame.font.Font(font_path, 90)

        self.lanes = []
        for i in range(LANE_COUNT):
            lane = Lane()
            lane.x = i * int(lane.space + lane.width)
            self.lanes.append(lane)

        self.cars = []
        for i in range(CAR_COUNT):
            car = Car()
            self.cars.append(car)
        self.player = Car()

        self.score = 0

        self.highscore = 0

        self.menu_on = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.menu_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        pygame.mouse.set_visible(False)
                        self.score = 0
                        self.highscore = 0
                        self.menu_on = False
                        self.player.load()
                        for car in self.cars:
                            car.load_random()
                        
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.dy -= random.randint(6,7)
                    elif event.key == pygame.K_DOWN:
                        self.player.dy += random.randint(6,7)
                    elif event.key == pygame.K_LEFT:
                        self.player.dx -= random.randint(6,7)
                    elif event.key == pygame.K_RIGHT:
                        self.player.dx += random.randint(6,7)
                    elif event.key == pygame.K_p:
                        self.score += 54378294552345325
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.dx = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player.dy = 0

        return False

    def run_logic(self, screen):
        for car in self.cars:
            if car.y > SCREEN_HEIGHT:
                self.score += random.randrange(0,21)
                self.highscore += 10
                car.load_random()

            if self.player.check_crash(car):
                self.menu_on = True
                pygame.mixer.music.stop()
                self.player.crash_sound.play()
                self.player.draw_crash(screen)
                car.draw_crash(screen)
                sleep(1)
                pygame.mouse.set_visible(True)

            """ for com in self.cars:
                if car == com:
                    None
                elif car.check_crash(com):
                    self.score += 10
                    car.collision_sound.play()
                    car.draw_crash(screen)
                    car.load_random()
                    com.draw_crash(screen)
                    com.load_random() """

    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    def display_menu(self, screen):
        screen.fill(GRAY)   
        
        screen.blit(self.djrRK_image, [1300, 350])
        screen.blit(self.image_intro, [1025, 150])
        draw_x = int(SCREEN_WIDTH / 2)
        draw_y = int(SCREEN_HEIGHT / 2)
        self.draw_text(screen, "수동차 게임",
                       self.font_90, draw_x, draw_y + 50, BLACK)
        self.draw_text(screen, "점수: " + str(self.score),
                       self.font_40, draw_x, draw_y + 150, WHITE)
        self.draw_text(screen, "스페이스키를 눌러 시작",
                       self.font_30, draw_x, draw_y + 200, RED)


    def display_frame(self, screen):
        screen.fill(GRAY)   

        for lane in self.lanes:
            lane.move(SPEED, screen)

        self.player.draw(screen)
        self.player.move()
        self.player.out_of_screen()

        for car in self.cars:
            car.draw(screen)
            car.move()

        self.draw_text(screen, "점수: " + str(self.score),
                       self.font_30, 80, 20, BLACK)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    pygame.init()
    pygame.display.set_caption("수동차 게임")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()