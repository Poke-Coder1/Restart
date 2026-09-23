import turtle
import math
import random
import time

WIDTH = 1000
HEIGHT = 850

SCALE = 15

NUM_LINES = 2200

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Flowing Heart")

screen.tracer(0, 0)

turtle.colormode(255)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def heart(t):
    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    )
    return x * SCALE, y * SCALE

for i in range(NUM_LINES):
    t = 2 * math.pi * i / NUM_LINES
    x1, y1 = heart(t)

    inner_scale = random.uniform(0.95, 0.5)
    x2 = x1 * inner_scale
    y2 = y1 * inner_scale

    color_type = random.random()

    if color_type < 0.55:
        red = random.randint(190, 255)
        green = random.randint(55, 125)
        blue = random.randint(105, 175)
    
    elif color_type < 0.85:
        red = random.randint(230, 255)
        green = random.randint(120, 190)
        blue = random.randint(160, 220)
    
    else:
        red = random.randint(120, 200)
        green = random.randint(35, 90)
        blue = random.randint(100, 170)
    
    pen.pencolor(red, green, blue)

    pen.width(random.choice([1, 1, 1, 1, 2]))

    pen.goto(x1, y1)
    pen.pendown()

    pen.goto(x2, y2)

    pen.penup()

    if i % 20 == 0:
        screen.update()


for layer in range(3):

    pen.width(1)

    if layer == 0:
        pen.pencolor(255, 120, 180)
    elif layer == 1:
        pen.pencolor(230, 70, 145)
    else:
        pen.pencolor(180, 50, 120)

    previous = None

    for i in range(401):

        t = 2 * math.pi * i / 400

        x, y = heart(t)

        factor = 1 - layer * 0.008

        x *= factor
        y *= factor 

        if previous is not None:
            pen.goto(previous[0], previous[1])
            pen.pendown()
            pen.goto(x, y)
            pen.penup()
        
        previous = (x, y)

screen.update()
time.sleep(2)
turtle.done()