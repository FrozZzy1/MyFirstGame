import pygame as pg
from random import randint as rd
import time
clock = pg.time.Clock()
pg.init()
FPS = 60
сlock = pg.time.Clock()
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
enemyLeft = pg.image.load('textures/enemyLeft.png')
enemyRight = pg.image.load('textures/enemyRight.png')
enemy_chest_L = pg.image.load('textures/enemy_chest_L.png')
enemy_chest_R = pg.image.load('textures/enemy_chest_R.png')
pickaxe_helmet = pg.image.load('textures/pickaxe_helmet.png')
dagger = pg.image.load('textures/dagger.png')
chest1 = pg.image.load('textures/chest.png')
open_chest = pg.image.load('textures/open_chest.png')
esc_menu = pg.image.load('textures/esc_menu.png')
esc_1 = pg.image.load('textures/esc_1.png')
esc_2 = pg.image.load('textures/esc_2.png')
esc_3 = pg.image.load('textures/esc_3.png')

x_enemy = 1000
y_enemy = rd(435, 550)
xp = 640
yp = 500
x_dagger = 0
y_dagger = 0
step = 200
step_enemy = 100
step_shot = 300
n = 1400
xb, yb = 0, 0
x_chest = 80
y_chest = 540
x_openchest = 50
look_player_r = False
look_enemy_r = False
move_enemy_r = False
enemychest = False
last_time = time.time()
shot = False 

def chest():
    global x_chest, y_chest
    if abs(x_enemy - x_chest) < 100 and y_chest+50 >= y_enemy >= y_chest-50:
        screen.blit(open_chest, (x_openchest, y_chest))
    else:
        screen.blit(chest1, (x_chest, y_chest))
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
    global look_player_r, delta_t, last_time, xp, yp, step, keys
    delta_t = time.time() - last_time
    last_time = time.time()
    keys = pg.key.get_pressed()
    if not look_player_r:
        screen.blit(playerR, (xp, yp))
        screen.blit(swordR, (xp, yp))
    else:
        screen.blit(swordL, (xp,yp))
        screen.blit(playerL, (xp, yp))
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

def move_enemy():
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r, enemychest
    if x_enemy >= 1000:
        move_enemy_r = False
        enemychest = False
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
        enemychest = True
        screen.blit(enemy_chest_R, (x_enemy, y_enemy))
        screen.blit(pickaxe_helmet, (100, 560))


    
def esc_game():
    global run_game
    run_esc = True
    while run_esc:
        pos = pg.mouse.get_pos()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            if 660 >= pos[0] >= 0 and 510 >= pos[1] >= 410:
                screen.blit(esc_1, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    run_game = True
                    run_esc = False
            elif 535 >= pos[0] >= 15 and 595 >= pos[1] >= 525:
                screen.blit(esc_2, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    menu2()
                    run_esc = False
            elif 200 >= pos[0] >= 10 and 720 >= pos[1] >= 635:
                screen.blit(esc_3, (0,0))
                if e.type == pg.MOUSEBUTTONDOWN:
                    quit()
            else:
                screen.blit(esc_menu, (0,0))
        pg.display.update()


def menu2():
    run_menu = True
    while run_menu:
        pos = pg.mouse.get_pos()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            menu(e)
            if 900 >= pos[0] >= 430 and 275 >= pos[1] >= 200 and e.type == pg.MOUSEBUTTONDOWN:
                run_menu = False
                run_game = True
        pg.display.update()
        сlock.tick(FPS)
    return run_game
run_game = menu2()

def game(run_game):
    global   shot, x_dagger, y_dagger
    while run_game:
        screen.blit(background, (0,0))
        if not enemychest:
            chest()
        move_player()
        move_enemy()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            if e.key == pg.K_ESCAPE:
                esc_game()
                
        pg.display.update()
        сlock.tick(FPS)

menu2()
game(run_game)
