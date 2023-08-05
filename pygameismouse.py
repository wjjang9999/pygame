import pygame as py
import os
import random

screen_width = 800
screen_height = 600

done = False

land = (255,254,255)


py.init()
py.display.set_caption("mouse")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()

#이미지 불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
mouse_image = py.image.load(os.path.join(assets_path,'mouse.png'))
mouse_x = int(screen_width / 2)
mouse_y = int(screen_height / 2)
py.mouse.set_visible(False)
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료

#게임 로직 구간
    pos = py.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
#화면 삭제 구간

#스크린 채우기
    screen.fill(land)

    screen.blit(mouse_image,[mouse_x,mouse_y])
#화면 그리기 구간

    #화면 업데이트
    py.display.flip()
#초당 120 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()

