import turtle as t
import random

oogway = t.Turtle()
t.colormode(255)


def Rand_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(g):
    oogway.speed(0)
    oogway.pensize(15)
    for i in range(g):
        oogway.pencolor(Rand_colour())
        p = random.randint(0,360)
        oogway.setheading(p)
        oogway.forward(30)


random_walk(250)


screen = t.Screen()
screen.exitonclick()
