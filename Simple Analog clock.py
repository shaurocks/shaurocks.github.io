# Simple Analog clock
# by Shaurocks
# my second project

import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=680, height=600)
wn.title("Simple Clock by Shaurocks")
wn.tracer(0)

# drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("red")
    pen.pendown()
    pen.circle(210)

    # draw hour lines
    pen.penup()
    pen.color("orange")
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    # Draw hourhand
    pen.penup()
    pen.color("blue")
    pen.goto(0,0)
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw minutehand
    pen.penup()
    pen.color("purple")
    pen.goto(0,0)
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Draw secondhand
    pen.penup()
    pen.color("pink")
    pen.goto(0,0)
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, pen)
    wn.update()
    
    time.sleep(1)
    
    pen.clear()

wn.mainloop()