import turtle
import math
t = turtle.Turtle()
def rohiticalcoding(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.speed(10)
def round(r, color,):
    x_point = 0
    y_point = -r
    rohiticalcoding(x_point,y_point)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
def pandav(r,color)
    rohiticalcoding(0, 0)
    t.pencolor(color)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
        t.right(144)
    t.end_fill()
    t.hideturtle()


if _name_ == '_main_':
    round(288, 'crimson')
    round(234, 'snow')
    round(174, 'crimson')
    round(114, 'blue')
    pandav(114, 'snow')
    turtle.done()