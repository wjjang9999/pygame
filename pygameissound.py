import pygame as py
import os
import time

screen_width = 640
screen_height = 400

done = False

black = (0,0,0)

py.init()
py.display.set_caption("sound")
screen = py.display.set_mode((screen_width,screen_height))
clock = py.time.Clock()
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
background_image = py.image.load(os.path.join(assets_path, 'equalizer.png'))
py.mixer.music.load(os.path.join(assets_path,'bgm.wav'))
py.mixer.music.play(-1)
sound = py.mixer.Sound(os.path.join(assets_path, '폭발.wav'))
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:#창이 닫히는 이벤트 발생시
            done = True #반복 중단 -> 게임 종료
        if event.type == py.MOUSEBUTTONDOWN:
            sound.play()
            time.sleep(0.25)
            sound.play()
            time.sleep(0.25)
            sound.play()
            time.sleep(0.25)
            sound.play()
            time.sleep(0.25)
            sound.play()
            time.sleep(0.25)
#게임 로직  구간

    
#화면 삭제 구간

#스크린 채우기
    screen.fill(black)

    screen.blit(background_image, background_image.get_rect())
#화면 그리기 구간

#화면 업데이트
    py.display.flip()
#초당 120 프레임으로 업데이트
    clock.tick(120)
#게임 종료 
py.quit()
