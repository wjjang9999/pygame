import pygame as py
import time
import random

screen_width = 600
screen_height = 600
done = False

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
ball_dx = 7.1
ball_dy = 8.3
ball_size = 40

py.init()
py.display.set_caption("pygame test")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료

#게임 로직 구간

    ball_x += ball_dx
    ball_y += ball_dy

    if (ball_x + ball_size) > screen_width or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1.01
    if (ball_y + ball_size) > screen_height or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1.01
#화면 삭제 구간

#스크린 채우기
    screen.fill(white)
#화면 그리기 구간
    py.draw.circle(screen,blue, [ball_x,ball_y], ball_size , 0)

#화면 업데이트
    py.display.flip()
#초당 60? 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()
