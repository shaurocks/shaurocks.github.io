# writting
# shaurocks
# python

import turtle
import time

# add background
bg=turtle.Screen()
bg.title("writting by shaurocks")
bg.setup(width= 600, height= 600)
bg.bgcolor("black")
bg.tracer(0)# Turns off the screen updates


# add writting pen
pen = turtle.Turtle()
pen.penup()
pen.pensize(5)
pen.goto(0,0)
pen.pencolor("light blue")



while True:
        h = int(time.strftime("%I"))
        m = int(time.strftime("%M"))
        s = int(time.strftime("%S"))
        pen.color("light blue")
        pen.clear()
        pen.pendown
        pen.pensize(5)
        pen.write((h, m, s),  align="center", font=("courier", 24, "normal"))

        
        


bg.mainloop()