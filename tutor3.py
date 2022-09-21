import pygame as pg
import random as r

pg.init()

screen_width = 1000
screen_height = int(screen_width/16*9)

window = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption("Drawing Test")

run = True
curPos = [0, 0]
color = [0, 0, 255]
size = 20
while(run):
    pg.time.delay(16)

    window.fill((200, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEMOTION:
            curPos[0] = event.pos[0]
            curPos[1] = event.pos[1]
        if event.type == pg.MOUSEBUTTONDOWN:
            # Set our color to random RGB values
            color = [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]
        if event.type == pg.MOUSEBUTTONUP:
            # Set our color to random RGB values
            size = r.randint(10, 200)

    pg.draw.circle(window, color, curPos, size)

    pg.display.update()
