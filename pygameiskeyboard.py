import pygame as py
import time
import os
import random

screen_width = 800
screen_height = 600

done = False

gray = (200,200,200)

py.init()
py.display.set_caption("keyboard")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
keyboard_image = py.image.load(os.path.join(assets_path, 'keyboard.png'))
keyboard_x = int(screen_width / 2)
keyboard_y = int(screen_height / 2)
keyboard_dx = 0
keyboard_dy = 0
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료

        elif event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                keyboard_dx = 5
            elif event.key == py.K_LEFT:
                keyboard_dx = -5
            elif event.key == py.K_UP:
                keyboard_dy = -5
            elif event.key == py.K_DOWN:
                keyboard_dy = 5
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                keyboard_dx = 0
            elif event.key == py.K_UP or event.key == py.K_DOWN:
                keyboard_dy = 0
#게임 로직 구간
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy
    
    if (keyboard_x + 63) > screen_width:
        keyboard_x = keyboard_x + -5
    if  keyboard_x < 0:
        keyboard_x = keyboard_x - -5
    if (keyboard_y + 50) > screen_height:
        keyboard_y = keyboard_y + -5
    if (keyboard_y + 12) < 0:
        keyboard_y = keyboard_y - -5
#화면 삭제 구간

#스크린 채우기
    screen.fill(gray)
#화면 그리기 구간
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])
#화면 업데이트
    py.display.flip()
#초당 60 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()
