import pygame
import os
import sys
import random

white = (254,254,254)
black = (0,0,0)
blue = (20,60,120)
orange = (250,170,70)
red = (250,0,0)

enemy_level = 150

screen_width = 800
screen_height = 1000
current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, 'assets')

class Ball():
    def __init__(self,bounce_sound):
        self.rect = pygame.Rect(screen_width//2,screen_height//2,12,12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 10
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0:
            self.dx *= -1.01
            self.rect.left = 0
            self.bounce_sound.play()
        elif self.rect.right > screen_width:
            self.dx *= -1.01
            self.rect.right = screen_width
            self.bounce_sound.play()
    def reset(self,x,y):
        self.rect.x =x
        self.rect.y = y
        self.dx = random.randint(-3,3)
        self.dy = 10
    def draw(self,screen):
        pygame.draw.rect(screen,orange,self.rect)

class Player():
    def __init__(self,ping_sound):
        self.rect = pygame.Rect(screen_width//2,screen_height-40,800,70)
        self.ping_sound = ping_sound
        self.dx = 0
    def update(self, ball):
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= screen_width and self.dx > 0:
            self.dx = 0
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5,5)
            ball.dy *= -1.01
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()

        self.rect.x += self.dx
    
    def draw(self,screen):
        pygame.draw.rect(screen,red,self.rect)
class Enemy():
    def __init__(self,pong_sound):
        self.rect = pygame.Rect(screen_width//2,25,3000,70)
        self.pong_sound = pong_sound

    def update(self, ball):
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff <= enemy_level:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x -= enemy_level
        elif self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            if diff <= enemy_level:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += enemy_level
        if self.rect.colliderect(ball.rect):
            ball.dy *= -1.01
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()
    def draw(self,screen):
        pygame.draw.rect(screen,black,self.rect,0)
class Game():
    def __init__(self):
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path, 'bounce.wav'))

        ping_sound = pygame.mixer.Sound(os.path.join(assets_path, 'ping.wav'))

        pong_sound = pygame.mixer.Sound(os.path.join(assets_path, 'pong.wav'))

        
        
        self.font = pygame.font.SysFont("malgungothic",50,False,False)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx = -5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0

        return True
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

        if self.ball.rect.top < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery)

        if self.ball.rect.bottom > screen_height:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx,self.enemy.rect.centery)
    def display_message(self,message,screen,color):
        labal = self.font.render(message, True, color)
        width = labal.get_width()
        height = labal.get_height()
        pos_x = screen_width//2 - (width/2)
        pos_y = screen_height//2 - (height/2)
        screen.blit(labal, (pos_x,pos_y))
        pygame.display.update()
    def display_frame(self,screen):
        screen.fill(blue)

        if self.player_score == 10000:
            self.display_message(screen, "승리", white)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)

        elif self.enemy_score == 10000:
            self.display_message(screen,"패배",white)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)
            for x in range(0,screen_width,24):
                pygame.draw.rect(screen,white,[x,screen_height//2,10,10])
            enemy_score_label = self.font.render(str(self.enemy_score), True, white)
            screen.blit(enemy_score_label, (10,400))
            player_score_label = self.font.render(str(self.player_score),True,white)
            screen.blit(player_score_label,(10,540)) 

def main():
    pygame.init()
    pygame.display.set_caption("핑퐁게임")
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    running = True

    game = Game()

    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
if __name__ == '__main__':
    main()
