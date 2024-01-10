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
    k = [1, 2, 3, 4]
    oogway.speed(0)
    oogway.pensize(15)
    for i in range(g):
        oogway.pencolor(Rand_colour())
        p = random.choice(k)
        if p == 1:
            oogway.forward(30)
        elif p == 2:
            oogway.backward(30)
        elif p == 3:
            oogway.right(90)
            oogway.forward(30)
        elif p == 4:
            oogway.left(90)
            oogway.forward(30)


random_walk(250)


screen = t.Screen()
screen.exitonclick()
