import pygame as pg
from random import randint as rd
import time
clock = pg.time.Clock()
pg.init()
FPS = 90
fpsClock = pg.time.Clock()
pg.display.set_caption('Defender of the Forest')

screenX = 1280
screenY = 720
screen = pg.display.set_mode((screenX, screenY))
background = pg.image.load('textures/background.png')
start_screen = pg.image.load('textures/start_screen.png')
start_screen_1 = pg.image.load('textures/start_screen_1.png')
start_screen_2 = pg.image.load('textures/start_screen_2.png')
start_screen_3 = pg.image.load('textures/start_screen_3.png')
screen_howtoplay = pg.image.load('textures/screen_howtoplay.png')
screen_howtoplay2 = pg.image.load('textures/screen_howtoplay2.png')
screen_management = pg.image.load('textures/screen_management.png')
management_backtomenu = pg.image.load('textures/management_backtomenu.png')
management_backtomenu2 = pg.image.load('textures/management_backtomenu2.png')
playerL = pg.image.load('textures/playerSwordL.png')
playerR = pg.image.load('textures/playerSwordR.png')
swordR = pg.image.load('textures/SwordR.png')
swordL = pg.image.load('textures/SwordL.png')
<<<<<<< HEAD
enemy = pg.image.load('textures/enemy.png')
=======
enemyLeft = pg.image.load('textures/enemyLeft.png')
enemyRight = pg.image.load('textures/enemyRight.png')
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
dagger = pg.image.load('textures/dagger.png')
chest1 = pg.image.load('textures/chest.png')
chest2 = pg.image.load('textures/chest.png')
chest3 = pg.image.load('textures/chest.png')
open_chest1 = pg.image.load('textures/open_chest.png')
open_chest2 = pg.image.load('textures/open_chest.png')
open_chest3 = pg.image.load('textures/open_chest.png')

x_enemy = 1000
y_enemy = rd(435, 550)
xp = 640
yp = 500
step = 200
step_enemy = 100
step_shot = 10
n = 1400
xb, yb = 0, 0
xdagger = xp + 55
ydagger = yp + 55
x_chest = 80
y_chest1 = 500
y_chest2 = 540
y_chest3 = 580
x_openchest = 50
<<<<<<< HEAD
look_r = False
shot = False
=======
look_player_r = False
look_enemy_r = False
move_enemy_r = False
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
last_time = time.time()

def chests():
    global x_chest, y_chest1, y_chest2, y_chest3

<<<<<<< HEAD
    if abs(x_enemy - x_chest) < 100 and y_chest1+100 >= y_enemy >= y_chest1-100:
        screen.blit(open_chest1, (x_openchest, y_chest1))
    else:
        screen.blit(chest1, (x_chest, y_chest1))
    if abs(x_enemy - x_chest) < 100 and y_chest2+100 >= y_enemy >= y_chest2-100:
        screen.blit(open_chest2, (x_openchest, y_chest2))
    else:
        screen.blit(chest2, (x_chest, y_chest2))
    if abs(x_enemy - x_chest) < 100 and y_chest3+100 >= y_enemy >= y_chest3-100:
=======
    if abs(x_enemy - x_chest) < 100 and y_chest1+50 >= y_enemy >= y_chest1-50:
        screen.blit(open_chest1, (x_openchest, y_chest1))
    else:
        screen.blit(chest1, (x_chest, y_chest1))
    if abs(x_enemy - x_chest) < 100 and y_chest2+50 >= y_enemy >= y_chest2-50:
        screen.blit(open_chest2, (x_openchest, y_chest2))
    else:
        screen.blit(chest2, (x_chest, y_chest2))
    if abs(x_enemy - x_chest) < 100 and y_chest3+50 >= y_enemy >= y_chest3-50:
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
        screen.blit(open_chest3, (x_openchest, y_chest3))
    else:
        screen.blit(chest3, (x_chest, y_chest3))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit()
    pg.display.update()

def backtomenu():
    running = True
    while running:
        pos = pg.mouse.get_pos()
        for e in pg.event.get():
            if 870 <= pos[0] <= 1250 and 655 <= pos[1] <= 705:
                screen.blit(management_backtomenu2, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    running = False
            else:
                screen.blit(management_backtomenu, (0,0))
            if e.type == pg.QUIT:
                quit()
        pg.display.update()
        
def howtoplay():
    running = True
    while running:
        pos = pg.mouse.get_pos()
        
        
        for e in pg.event.get():
            if 710 <= pos[0] <= 1280 and 620 <= pos[1] <= 690:
                screen.blit(screen_howtoplay2, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    running = False
            elif 20 <= pos[0] <= 390 and 390 <= pos[1] <= 690:
                screen.blit(screen_management, (0,0))
            else:
                screen.blit(screen_howtoplay, (0,0))
            if 20 <= pos[0] <= 390 and 390 <= pos[1] <= 690 and e.type == pg.MOUSEBUTTONDOWN:
                backtomenu()
                
            if e.type == pg.QUIT:
                quit()
        pg.display.update()



def menu(e):
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


def move_player():
<<<<<<< HEAD
    global look_r, delta_t, last_time, xp, yp, step
=======
    global look_player_r, delta_t, last_time, xp, yp, step
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
    delta_t = time.time() - last_time
    last_time = time.time()
    keys = pg.key.get_pressed()
    if keys[pg.K_d] and xp < 1200:
        look_player_r = False
        xp = xp + step*delta_t
    if keys[pg.K_a] and xp > 45:
        look_player_r = True
        xp = xp - step*delta_t
    if keys[pg.K_w] and yp > 435:
        yp = yp - step*delta_t
    if keys[pg.K_s] and yp < 550:
        yp = yp + step*delta_t
<<<<<<< HEAD
    if not look_r:
=======
    if not look_player_r:
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
        screen.blit(playerR, (xp, yp))
        screen.blit(swordR, (xp, yp))
    else:
        screen.blit(swordL, (xp,yp))
        screen.blit(playerL, (xp, yp))

def move_enemy():
<<<<<<< HEAD
    global x_enemy
    if x_enemy > 100:
        x_enemy = x_enemy-step_enemy*delta_t
    else:
        x_enemy = 1000
    screen.blit(enemy, (x_enemy, y_enemy))
=======
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r
    if x_enemy >= 1000:
        move_enemy_r = False
    if not move_enemy_r:
        look_enemy_r = False
        x_enemy = x_enemy-step_enemy*delta_t
    if x_enemy <= 100:
        move_enemy_r = True
    if move_enemy_r:
        look_enemy_r = True
        x_enemy = x_enemy+step_enemy*delta_t

    if not look_enemy_r:
        screen.blit(enemyLeft, (x_enemy, y_enemy))
    else:
        screen.blit(enemyRight, (x_enemy, y_enemy))
        screen.blit(chest1, (x_enemy+40, y_enemy+40))
    
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32


def game():
    while True:
        screen.blit(background, (0,0))
        chests()
        move_player()
        move_enemy()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
        pg.display.update()


    
while True:
    pos = pg.mouse.get_pos()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        menu(e)
        if 900 >= pos[0] >= 430 and 275 >= pos[1] >= 200 and e.type == pg.MOUSEBUTTONDOWN:
            game()
    pg.display.update()
<<<<<<< HEAD
=======
    fpsClock.tick(FPS)
>>>>>>> ff2e71d4ea9cc0df8e688cec1ac1f8a5eac27c32
