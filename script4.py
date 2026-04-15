from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(3)

h = 0

def color_random():
    global h
    color(hsv_to_rgb(h, 1, 1))
    h += 0.02

def linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# F
color_random()
linea(-300, 100, -300, -100)
linea(-300, 100, -250, 100)
linea(-300, 0, -250, 0)

# E
color_random()
linea(-220, 100, -220, -100)
linea(-220, 100, -170, 100)
linea(-220, 0, -180, 0)
linea(-220, -100, -170, -100)

# R
color_random()
linea(-140, 100, -140, -100)
linea(-140, 100, -90, 100)
linea(-140, 0, -90, 0)
linea(-90, 100, -90, 0)
linea(-140, 0, -90, -100)

# N
color_random()
linea(-60, -100, -60, 100)
linea(-60, 100, -10, -100)
linea(-10, -100, -10, 100)

# A
color_random()
linea(20, -100, 45, 100)
linea(70, -100, 45, 100)
linea(30, 0, 60, 0)

# N
color_random()
linea(100, -100, 100, 100)
linea(100, 100, 150, -100)
linea(150, -100, 150, 100)

# D
color_random()
linea(180, 100, 180, -100)
linea(180, 100, 230, 50)
linea(230, 50, 230, -50)
linea(230, -50, 180, -100)

# O
color_random()
penup()
goto(280, 0)
pendown()
circle(50)

hideturtle()
done()