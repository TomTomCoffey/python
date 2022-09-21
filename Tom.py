
import turtle
import colorsys



t= turtle.Turtle()
s = turtle.Screen()
t.speed(0)
n = 36
h = 0
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0)
    h+=1/n 
    t.left(50)
    for j in range(5):
        t.forward(100)
        t.left(1500)
        t.back(2)