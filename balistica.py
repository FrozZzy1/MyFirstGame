import pygame as pg
from math import cos, sin, radians
import mygame as mg

def coordinates():
    x_shot0 = mg.xp + 30
    y_shot0 = mg.yp + 30
    look_shot_new = mg.look_player_r
    return x_shot0, y_shot0, look_shot_new

time_shot = 0
a = radians(45)
cosA = cos(a)
sinA = sin(a)
g = 30
v = 100
balistic_bool = False
shuriken = pg.image.load('textures/shuriken.png')

def balistic_shot():
    global x_shot, y_shot, time_shot, balistic_bool, x_shot0, y_shot0, look_shot_new, enemy_count_hp
    if not balistic_bool:
        x_shot0, y_shot0, look_shot_new = coordinates()
    if balistic_bool:
        if not look_shot_new:
            x_shot = x_shot0 + v * cosA * time_shot
        else:
            x_shot = x_shot0 - v * cosA * time_shot
        y_shot = y_shot0 - (v * sinA * time_shot - g * time_shot ** 2 / 2)
        time_shot = time_shot + 0.05
        mg.screen.blit(shuriken, (x_shot, y_shot))
        if y_shot >= y_shot0 + 50 or mg.screenX <= x_shot <= 0:
            balistic_bool = False
            x_shot, y_shot = 0, 0
            time_shot = 0
        if mg.x_enemy + 50 >= x_shot >= mg.x_enemy and mg.y_enemy + 50 >= y_shot >= mg.y_enemy + 10:
            balistic_bool = False
            x_shot, y_shot = 0, 0
            time_shot = 0
            mg.enemy_count_hp -= 1