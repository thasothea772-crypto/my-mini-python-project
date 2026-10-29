import turtle
import math
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.setup(800, 800)

t.speed(0)
t.width(2)
t.hideturtle()

for i in range(360):
    h = (0.85 + i / 720) % 1.0
    c = colorsys.hsv_to_rgb(h, 0.9, 1)

    t.pencolor(c)

    r = 220 * math.sin(math.radians(6 * i))

    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(2)

turtle.done
