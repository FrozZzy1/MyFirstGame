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
start_screen = pg.image.load('textures/start_screen/start_screen.png')
start_screen_1 = pg.image.load('textures/start_screen/start_screen_1.png')
start_screen_2 = pg.image.load('textures/start_screen/start_screen_2.png')
start_screen_3 = pg.image.load('textures/start_screen/start_screen_3.png')
screen_howtoplay = pg.image.load('textures/howtoplay/screen_howtoplay.png')
screen_howtoplay2 = pg.image.load('textures/howtoplay/screen_howtoplay2.png')
screen_management = pg.image.load('textures/howtoplay/screen_management.png')
management_backtomenu = pg.image.load('textures/howtoplay/management_backtomenu.png')
management_backtomenu2 = pg.image.load('textures/howtoplay/management_backtomenu2.png')
enemyLeft = pg.image.load('textures/enemy/enemyLeft.png')
enemyRight = pg.image.load('textures/enemy/enemyRight.png')
enemy_chest_L = pg.image.load('textures/enemy/enemy_chest_L.png')
enemy_chest_R = pg.image.load('textures/enemy/enemy_chest_R.png')
pickaxe_helmet = pg.image.load('textures/pickaxe_helmet.png')
daggerRight = pg.image.load('textures/daggerRight.png')
daggerLeft = pg.image.load('textures/daggerLeft.png')

x_enemy = 1000
y_enemy = rd(435, 550)
xp = 640
yp = 500
x_dagger = xp + 55
y_dagger = yp + 55
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
bool_shot = False
run_esc = False


chest1 = pg.image.load('textures/chest.png')
open_chest = pg.image.load('textures/open_chest.png')

def chest():
    global x_chest, y_chest
    if not enemychest:
        if abs(x_enemy - x_chest) < 100 and y_chest+50 >= y_enemy >= y_chest-50:
            screen.blit(open_chest, (x_openchest, y_chest))
        else:
            screen.blit(chest1, (x_chest, y_chest))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                quit()

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
    pg.display.update()


playerL0 = pg.image.load('textures/player/playerSwordL0.png')
playerL1 = pg.image.load('textures/player/playerSwordL1.png')
playerL2 = pg.image.load('textures/player/playerSwordL2.png')
playerL3 = pg.image.load('textures/player/playerSwordL3.png')
playerL4 = pg.image.load('textures/player/playerSwordL4.png')
playerR0 = pg.image.load('textures/player/playerSwordR0.png')
playerR1 = pg.image.load('textures/player/playerSwordR1.png')
playerR2 = pg.image.load('textures/player/playerSwordR2.png')
playerR3 = pg.image.load('textures/player/playerSwordR3.png')
playerR4 = pg.image.load('textures/player/playerSwordR4.png')
playerR = [playerR0, playerR1, playerR2, playerR3, playerR4]
playerL = [playerL0, playerL1, playerL2, playerL3, playerL4]
anim_point_player = 40
animation_hit = False
def anim_player(playerR, playerL):
    global animation_hit, xp, yp, anim_point_player
    if not look_player_r:
        if anim_point_player >= 36:
            screen.blit(playerR[1], (xp, yp))
        elif 35 >= anim_point_player >= 31:
            screen.blit(playerR[2], (xp, yp))
        elif 30 >= anim_point_player >= 26:
            screen.blit(playerR[3], (xp, yp))
        elif 25 >= anim_point_player >= 21:
            screen.blit(playerR[4], (xp, yp))
        elif 20 >= anim_point_player >= 16:
            screen.blit(playerR[3], (xp, yp))
        elif 15 >= anim_point_player >= 11:
            screen.blit(playerR[2], (xp, yp))
        elif 10 >= anim_point_player >= 6:
            screen.blit(playerR[1], (xp, yp))
        elif 5 >= anim_point_player >= 1:
            screen.blit(playerR[0], (xp, yp))
        elif anim_point_player <= 0:
            animation_hit = False
            anim_point_player = 40
        anim_point_player -= 2.5
    elif look_player_r:
        if anim_point_player >= 36:
            screen.blit(playerL[1], (xp, yp))
        elif 35 >= anim_point_player >= 31:
            screen.blit(playerL[2], (xp, yp))
        elif 30 >= anim_point_player >= 26:
            screen.blit(playerL[3], (xp, yp))
        elif 25 >= anim_point_player >= 21:
            screen.blit(playerL[4], (xp, yp))
        elif 20 >= anim_point_player >= 16:
            screen.blit(playerL[3], (xp, yp))
        elif 15 >= anim_point_player >= 11:
            screen.blit(playerL[2], (xp, yp))
        elif 10 >= anim_point_player >= 6:
            screen.blit(playerL[1], (xp, yp))
        elif 5 >= anim_point_player >= 1:
            screen.blit(playerL[0], (xp, yp))
        elif anim_point_player <= 0:
            animation_hit = False
            anim_point_player = 40
        anim_point_player -= 2.5




def move_player():
    global look_player_r, delta_t, last_time, xp, yp, step, keys, timer_player, animation_hit
    delta_t = time.time() - last_time
    last_time = time.time()
    keys = pg.key.get_pressed()
    if not animation_hit:
        if not look_player_r:
            screen.blit(playerR1, (xp, yp))
        else:
            screen.blit(playerL1, (xp, yp))
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
    else:
        anim_player(playerR, playerL)


dead_enemy_bool = False
dead_point_enemy = 100
dead_enemy_left = pg.image.load('textures/enemy/dead_enemy_left.png')
dead_enemy_right = pg.image.load('textures/enemy/dead_enemy_right.png')

def dead_enemy():
    global x_enemy, y_enemy, dead_point_enemy, dead_enemy_bool
    if dead_point_enemy <= 1:
        x_enemy = 1000
        dead_enemy_bool = False
        dead_point_enemy = 100
    else:
        screen.blit(dead_enemy_left, (x_enemy, y_enemy))
    dead_point_enemy -= 1

def if_dead_enemy():
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r, enemychest, y_chest, random_x_enemy, dead_enemy_bool
    if anim_point_player <= 5 and not look_player_r and xp + 40 <= x_enemy <= xp + 80 and yp - 40 <= y_enemy <= yp + 120:
        dead_enemy_bool = True
    elif anim_point_player <= 5 and look_player_r and xp - 40 <= x_enemy + 40 <= xp + 40 and yp - 40 <= y_enemy <= yp + 120:
        dead_enemy_bool = True
    elif x_enemy + 80 >= x_dagger >= x_enemy and y_enemy + 80 >= y_dagger >= y_enemy:
        dead_enemy_bool = True

def move_enemy():
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r, enemychest, y_chest, random_x_enemy, dead_enemy_bool
    if_dead_enemy()
    if dead_enemy_bool:
        dead_enemy()
    else:
        if x_enemy >= 1000:
            move_enemy_r = False
            enemychest = False
            random_x_enemy = rd(200, 800)
        if not move_enemy_r:
            if y_enemy < y_chest and x_enemy < random_x_enemy:
                y_enemy = y_enemy + step_enemy*delta_t
            elif y_enemy > y_chest + 50 and x_enemy < random_x_enemy:
                y_enemy = y_enemy - step_enemy*delta_t
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



look_shot = 0

def shot():
    global bool_shot, step_shot, x_dagger, y_dagger, look_shot
    if bool_shot:
        if look_shot == 1: 
            x_dagger += step_shot*delta_t
            screen.blit(daggerRight, (x_dagger, y_dagger))
        elif look_shot == 2:
            x_dagger -= step_shot*delta_t
            screen.blit(daggerLeft, (x_dagger, y_dagger))
        if screenX <= x_dagger or x_dagger <= 0 or (x_enemy + 80 >= x_dagger >= x_enemy and y_enemy + 80 >= y_dagger >= y_enemy):
            bool_shot = False
    else:
        x_dagger = xp + 55
        y_dagger = yp + 55
        look_shot = look_dagger(look_shot)


    
esc_menu = pg.image.load('textures/esc/esc_menu.png')
esc_1 = pg.image.load('textures/esc/esc_1.png')
esc_2 = pg.image.load('textures/esc/esc_2.png')
esc_3 = pg.image.load('textures/esc/esc_3.png')

def esc_game():
    global run_game, run_esc
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


def menu2():
    global run_game
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
        сlock.tick(FPS)

def look_dagger(look_shot):
    if not look_player_r:
        look_shot = 1
    elif look_player_r:
        look_shot = 2
    return look_shot


def game():
    global run_esc, bool_shot, look_shot, look_player_r, animation_hit, x_dagger, y_dagger
    while run_game:
        screen.blit(background, (0,0))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    run_esc = True
                if e.key == pg.K_f:
                    look_dagger(look_shot)
                    bool_shot = True
                elif e.key == pg.K_SPACE:
                    animation_hit = True
        chest()
        move_player()
        move_enemy()
        esc_game()
        shot()
        сlock.tick(FPS)
        pg.display.flip()

menu2()
game()
