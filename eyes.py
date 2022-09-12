import turtle
from turtle import *
from time import sleep

turt = turtle.Turtle()
turt.color('red', 'blue')


def _circle(radius, x, y, _color):
    turt.penup()
    turt.fillcolor(_color, )
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


def eyes():
    b = "Black"
    r = "Red"
    bl = "blue"
    _circle(210, -22, -150, b)
    _circle(196, -20, -135, r)
    _circle(50, -20, 15, b)

    turt.color(b, bl)

    _circle(35, -120, -67, b)
    turt.color(r, bl)
    _circle(35, -130, -65, r)
    turt.color(b, bl)
    _circle(34, -120, -60, b)

    _circle(35, 98, -2, b)
    turt.color(r, b)
    _circle(35, 85, 0, r)
    turt.color(b, bl)
    _circle(34, 100, -10, b)

    _circle(35, -40, 155, b)
    turt.color(r, bl)
    _circle(35, -55, 150, r)
    turt.color(b, bl)
    _circle(34, -37, 148, b)
    turtle.hideturtle()


screensize(1920, 1080, "#f0f0f0")
turtle.Screen().bgcolor("#dceaf6")

pensize(5)
speed(9)
eyes()
sleep(30)
turtle.Screen()
