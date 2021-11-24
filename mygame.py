from math import e
import pygame as pg
from random import randint as rd
import time
clock = pg.time.Clock()
pg.init()
FPS = 60
сlock = pg.time.Clock()
pg.display.set_caption('Защитник леса')

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

xp = 640
yp = 500
x_dagger = xp + 55
y_dagger = yp + 55
step = 200
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



sword = pg.image.load('textures/sword.png')
swordY = 0
def move_player():
    global look_player_r, delta_t, last_time, xp, yp, step, animation_hit, swordY
    delta_t = time.time() - last_time
    last_time = time.time()
    keys = pg.key.get_pressed()
    if not dead_player_bool:
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
        swordY = yp
    else:
        screen.blit(sword, (xp, swordY))
        dead_player()



dead_enemy_bool = False
dead_point_enemy = 100
x_enemy = 1000
y_enemy = rd(435, 550)
step_enemy = 100
dead_enemy_left = pg.image.load('textures/enemy/dead_enemy_left.png')
dead_enemy_right = pg.image.load('textures/enemy/dead_enemy_right.png')
enemy_full_hp = pg.image.load('textures/enemy_hp/full.png')
enemy_half_hp = pg.image.load('textures/enemy_hp/half.png')
enemy_zero_hp = pg.image.load('textures/enemy_hp/zero.png')
enemy_count_hp = 3

def enemy_hp(enemy_count_hp):
    global dead_enemy_bool, enemychest
    if not enemychest:
        if enemy_count_hp == 3:
            screen.blit(enemy_full_hp, (x_enemy, y_enemy))
        elif enemy_count_hp == 2:
            screen.blit(enemy_half_hp, (x_enemy, y_enemy))
        elif enemy_count_hp <= 1:
            screen.blit(enemy_zero_hp, (x_enemy, y_enemy))
            dead_enemy_bool = True
    elif enemychest:
        if enemy_count_hp == 3:
            screen.blit(enemy_full_hp, (x_enemy+25, y_enemy))
        elif enemy_count_hp == 2:
            screen.blit(enemy_half_hp, (x_enemy+25, y_enemy))
        elif enemy_count_hp <= 1:
            screen.blit(enemy_zero_hp, (x_enemy+25, y_enemy))
            dead_enemy_bool = True

def dead_enemy():
    global x_enemy, y_enemy, dead_point_enemy, dead_enemy_bool, enemy_count_hp
    if dead_point_enemy <= 1:
        x_enemy = 1000
        y_enemy = rd(450, 550)
        dead_enemy_bool = False
        dead_point_enemy = 100
        enemy_count_hp = 3
    else:
        screen.blit(dead_enemy_left, (x_enemy, y_enemy))
    dead_point_enemy -= 1

def if_dead_enemy():
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r, enemychest, y_chest, random_x_enemy, dead_enemy_bool, enemy_count_hp
    enemy_hp(enemy_count_hp)
    if not enemychest:
        if anim_point_player <= 5 and not look_player_r and xp + 40 <= x_enemy <= xp + 80 and yp - 40 <= y_enemy <= yp + 120:
            enemy_count_hp -= 2
        elif anim_point_player <= 5 and look_player_r and xp - 40 <= x_enemy + 40 <= xp + 40 and yp - 40 <= y_enemy <= yp + 120:
            enemy_count_hp -= 2
        elif x_enemy + 80 >= x_dagger >= x_enemy and y_enemy + 80 >= y_dagger >= y_enemy:
            enemy_count_hp -= 1
    else:
        if anim_point_player <= 5 and not look_player_r and xp + 40 <= x_enemy <= xp + 80 and yp - 40 <= y_enemy <= yp + 120:
            enemy_count_hp -= 2
        elif anim_point_player <= 5 and look_player_r and xp - 40 <= x_enemy + 40 <= xp + 40 and yp - 40 <= y_enemy <= yp + 120:
            enemy_count_hp -= 2
        elif x_enemy + 80 >= x_dagger >= x_enemy and y_enemy + 100 >= y_dagger >= y_enemy - 20:
            enemy_count_hp -= 1

position = 40
y_step_enemy = 70
def move_enemy():
    global x_enemy, y_enemy, move_enemy_r, look_enemy_r, enemychest, random_x_enemy, y_chest, dead_enemy_bool, step_enemy, y_step_enemy, position
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
                y_enemy = y_enemy + y_step_enemy*delta_t
            elif y_enemy > y_chest + 30 and x_enemy < random_x_enemy:
                y_enemy = y_enemy - y_step_enemy*delta_t
            look_enemy_r = False
            x_enemy = x_enemy-step_enemy*delta_t
        if move_enemy_r:
            if 30 <= position <= 40 and 550 >= y_enemy >= 450:
                y_enemy = y_enemy - y_step_enemy*delta_t
            elif 10 <= position <= 20 and 550 >= y_enemy >= 450:
                y_enemy = y_enemy + y_step_enemy*delta_t
            position -= 0.1
        if position <= 0:
            position = 40
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
        


ghostR1 = pg.image.load('textures/ghost/ghostR1.png')
ghostL1 = pg.image.load('textures/ghost/ghostL1.png')
x_ghost = 100
y_ghost = rd(450, 550)
look_ghost = False
step_ghost = 80
step_ghostY = 20

def move_ghost():
    global x_ghost, y_ghost, look_ghost
    if 80 <= xp - x_ghost <= 400:
        x_ghost = x_ghost + step_ghost*delta_t
        look_ghost = False
    if 80 <= x_ghost - xp <= 400:
        x_ghost = x_ghost - step_ghost*delta_t
        look_ghost = True
    if 0 <= yp - y_ghost <= 400:
        y_ghost = y_ghost + step_ghostY*delta_t
    if 0 <= y_ghost - yp <= 400:
        y_ghost = y_ghost - step_ghostY*delta_t
    if not look_ghost:
        screen.blit(ghostR1, (x_ghost, y_ghost))
    elif look_ghost:
        screen.blit(ghostL1, (x_ghost, y_ghost))

hp_0 = pg.image.load('textures/hp/hp_0.png')
hp_1 = pg.image.load('textures/hp/hp_1.png')
hp_2 = pg.image.load('textures/hp/hp_2.png')
hp_3 = pg.image.load('textures/hp/hp_3.png')
hp_4 = pg.image.load('textures/hp/hp_4.png')
hp = 4
dead_player_bool = False

def hp_player():
    global hp, x_ghost, y_ghost, dead_player_bool
    if x_ghost <= xp <= x_ghost + 80 and y_ghost <= yp <= y_ghost + 10:
        x_ghost = 100
        y_ghost = rd(450, 550)
        hp -= 1
    if hp == 4:
        screen.blit(hp_4, (0, 0))
    elif hp == 3:
        screen.blit(hp_3, (0,0))
    elif hp == 2:
        screen.blit(hp_2, (0,0))
    elif hp == 1:
        screen.blit(hp_1, (0,0))
    elif hp <= 0:
        screen.blit(hp_0, (0,0))
        dead_player_bool = True

deadPlayerR= pg.image.load('textures/player/dead_playerR.png')
deadPlayerL= pg.image.load('textures/player/dead_playerL.png')

def dead_player():
    global yp, step, xp, dead_player_bool, hp
    yp = yp - step*delta_t
    if not look_player_r:
        screen.blit(deadPlayerR, (xp, yp))
    else:
        screen.blit(deadPlayerL, (xp, yp))
    if yp - 80 <= 0:
        dead_player_bool = False
        revival_player(xp, yp, hp)
        xp, yp, hp = revival_player(xp, yp, hp)

def revival_player(xp, yp, hp):
    xp = 640
    yp = 500
    hp = 4
    return xp, yp, hp


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
        x_dagger = 0
        y_dagger = 0
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
    return 1 if not look_player_r else 2

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
                    if not bool_shot:
                        x_dagger = xp + 55
                        y_dagger = yp + 55
                    bool_shot = True
                elif e.key == pg.K_SPACE:
                    animation_hit = True
        chest()
        move_player()
        move_enemy()
        move_ghost()
        esc_game()
        shot()
        hp_player()
        сlock.tick(FPS)
        pg.display.flip()

menu2()
game()
