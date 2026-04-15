from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
width(2)

h = 0

for i in range(200):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.01
    
    forward(i)
    right(59)

hideturtle()
done()