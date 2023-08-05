import pygame as py
import os
import random

screen_width = 640
screen_height = 320

done = False

land = (160,120,40)


py.init()
py.display.set_caption("image")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()

#이미지 불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
background_image = py.image.load(os.path.join(assets_path,'terrain.png'))
mushroom_image1 = py.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image2 = py.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image3 = py.image.load(os.path.join(assets_path, 'mushroom3.png')) 

while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료

#게임 로직 구간
    
#화면 삭제 구간

#스크린 채우기
    screen.fill(land)

    screen.blit(background_image, background_image.get_rect())
    screen.blit(mushroom_image1, [random.randrange(100,111),random.randrange(80,91)])
    screen.blit(mushroom_image2, [random.randrange(300,311),random.randrange(100,111)])
    screen.blit(mushroom_image3, [random.randrange(450,461),random.randrange(140,151)])
#화면 그리기 구간

    #화면 업데이트
    py.display.flip()
#초당 120 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()






