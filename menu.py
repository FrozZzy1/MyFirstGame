import pygame as pg
import time

from pygame.constants import MOUSEBUTTONDOWN
pg.init()

screenX = 1280
screenY= 720
screen = pg.display.set_mode((screenX, screenY))
background = pg.image.load('textures/background.png')
start_screen = pg.image.load('textures/start_screen.png')
start_screen_1 = pg.image.load('textures/start_screen_1.png')
start_screen_2 = pg.image.load('textures/start_screen_2.png')
start_screen_3 = pg.image.load('textures/start_screen_3.png')
screen_howtoplay = pg.image.load('textures/screen_howtoplay.png')
screen_howtoplay2 = pg.image.load('textures/screen_howtoplay2.png')
x = 0
y = 0
def howtoplay():
    running = True
    while running:
        if pg.mouse.get_focused():
            pos = pg.mouse.get_pos()
        
        pg.display.update()
        for e in pg.event.get():
            if 710 <= pos[0] <= 1280 and 620 <= pos[1] <= 690:
                screen.blit(screen_howtoplay2, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    running = False
            else:
                screen.blit(screen_howtoplay, (0,0))
                
            if e.type == pg.QUIT:
                quit()
            
def game():


def menu():
    global boop
    pos = pg.mouse.get_pos()
    if 900 >= pos[0] >= 430 and 275 >= pos[1] >= 200:
        screen.blit(start_screen_1, (0, 0))
    elif 840 >= pos[0] >= 485 and 380 >= pos[1] >= 300:
        screen.blit(start_screen_2, (0, 0))
    elif 740 >= pos[0] >= 585 and 480 >= pos[1] >= 415:
        screen.blit(start_screen_3, (0, 0))
        if e.type == pg.MOUSEBUTTONDOWN:
            quit()
    else:
        screen.blit(start_screen, (0, 0))
    if 840 >= pos[0] >= 485 and 380 >= pos[1] >= 300 and e.type == pg.MOUSEBUTTONDOWN:
        howtoplay()

            

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
        menu()
    pg.display.update()