import pygame as py
import time

screen_width = 800
screen_height = 600

done = False

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

py.init()
py.display.set_caption("pygame test")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료

#게임 로직 구간

#화면 삭제 구간

#스크린 채우기
    screen.fill(white)
#화면 그리기 구간

#화면 업데이트
    py.display.flip()
#초당 60 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()
