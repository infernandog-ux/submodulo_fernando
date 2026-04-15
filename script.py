import turtle
import random

pantalla = turtle.Screen()
pantalla.bgcolor("black")

lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.pensize(3)

colores = ["red", "blue", "green", "yellow", "purple", "orange", "white", "cyan"]

def dibujar_figura(lados, tamaño):
    angulo = 360 / lados
    lapiz.color(random.choice(colores))
    for i in range(lados):
        lapiz.forward(tamaño)
        lapiz.right(angulo)

for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    lapiz.penup()
    lapiz.goto(x, y)
    lapiz.pendown()

    lados = random.randint(3, 8)
    tamaño = random.randint(30, 80)
    dibujar_figura(lados, tamaño)

turtle.done()