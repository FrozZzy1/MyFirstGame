import pygame as pg
from random import randint as rd
import time
clock = pg.time.Clock()
pg.init()
screenX = 1280
screenY = 720
screen = pg.display.set_mode((screenX, screenY))
background = pg.image.load('textures/background.png')
playerL = pg.image.load('textures/playerSwordL.png')
playerR = pg.image.load('textures/playerSwordR.png')
swordR = pg.image.load('textures/SwordR.png')
swordL = pg.image.load('textures/SwordL.png')
enemy = pg.image.load('textures/enemy.png')

xe = 1000
ye = rd(435, 550)
xp = 640
yp = 500
step = 300
step_enemy = 80
n = 1400
look_r = False
last_time = time.time()
while True:
    delta_t = time.time() - last_time
    last_time = time.time()
    screen.blit(background, (0,0))
    keys = pg.key.get_pressed()
    if keys[pg.K_d] and xp < 1200:
        look_r = False
        xp = xp + step*delta_t
    if keys[pg.K_a] and xp > 45:
        look_r = True
        xp = xp - step*delta_t
    if keys[pg.K_w] and yp > 435:
        yp = yp - step*delta_t
    if keys[pg.K_s] and yp < 550:
        yp = yp + step*delta_t
    if xe > 100:
        xe = xe-step_enemy*delta_t
    else:
        xe = 1000
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    if not look_r:
        screen.blit(playerR, (xp, yp))
        screen.blit(swordR, (xp, yp))
    else:
        screen.blit(swordL, (xp,yp))
        screen.blit(playerL, (xp, yp))
    screen.blit(enemy, (xe, ye))
    pg.display.update()