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
    pg.time.delay(18)

    window.fill(225,0,0)

   

    

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
           curPos[0] = event.pos[0]
           sum = 0
           for curPos[1] in range(500):
                curPos[1] = curPos[1]+1
                sum+=1
                curPos[0] = sum
        #if(pg.event == pg.MOUSEWHEEL):
           # size = size + 20

    
                
                
  
       
            
                

    pg.draw.circle(window, color, curPos, size)

    pg.display.update()
