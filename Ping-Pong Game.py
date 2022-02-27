# Ping-pong AI version
# by shaurocks
# python 

import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping-pong by shaurocks")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# SCORE
score_a = 0
score_b = 0

# boundary
b = turtle.Turtle()
b.penup()
b.pencolor("white")
b.pensize("5")
b.goto(-390, 290)
b.pendown()
b.forward(780)
b.right(90)
b.forward(580)
b.right(90)
b.forward(780)
b.right(90)
b.forward(580)
b.hideturtle()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.pencolor("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.pendown()
pen.write("PLAYER A : 0   PLAYER B : 0", align="center", font=("courier", 24, "normal"))

# pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.pencolor("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(-500, -300)
pen2.pendown()
pen2.write("press key p to pause", align="center", font=("courier", 10, "normal"))

# pen3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.pencolor("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(500, -300)
pen3.pendown()
pen3.write("press key 1 to turn off Ai", align="center", font=("courier", 10, "normal"))

# pen4
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.pencolor("white")
pen4.penup()
pen4.hideturtle()
pen4.goto(-550, 0)
pen4.pendown()
pen4.write("use w,s to move", align="center", font=("courier", 10, "normal"))

# pen5
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.pencolor("white")
pen5.penup()
pen5.hideturtle()
pen5.goto(550, -0)
pen5.pendown()
pen5.write("use right,left arrow to move ", align="center", font=("courier", 10, "normal"))

# Fuction
def paddle_a_up():
        y = paddle_a.ycor()
        y += 15
        paddle_a.sety(y)

def paddle_a_down():
        y = paddle_a.ycor()
        y -= 15
        paddle_a.sety(y)

def paddle_b_up():
        y = paddle_b.ycor()
        y += 15
        paddle_b.sety(y)

def paddle_b_down():
        y = paddle_b.ycor()
        y -= 15
        paddle_b.sety(y)

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        
wn.listen()
wn.onkeypress(toggle_pause, "p") 

is_Ai = False

def toggle_ai():
    global is_Ai
    if is_Ai == True:
        is_Ai = False
    else:
        is_Ai = True      

wn.listen()
wn.onkeypress(toggle_ai, "1")

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    if not is_paused:
           wn.update()

           # move the ball
           ball.setx(ball.xcor() + ball.dx)
           ball.sety(ball.ycor() + ball.dy)

           # Border Checking
           if ball.ycor()> 290:
               ball.sety(290)
               ball.dy *= -1
               winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

           if ball.ycor()< -290:
               ball.sety(-290)
               ball.dy *= -1
               winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

           if ball.xcor()> 390:
               ball.setx(390)
               ball.dx *= -1
               score_a += 1
               winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
               pen.clear()
               pen.write("PLAYER A : {}   PLAYER B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
           if ball.xcor()< -390:
               ball.setx(-390)
               ball.dx *= -1
               score_b += 1
               winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
               pen.clear()
               pen.write("PLAYER A : {}   PLAYER B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

           # Paddle and ball collisions
           if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
                ball.setx(340)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
   
           if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
                ball.setx(-340)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

          
           # AI player
           if not is_Ai:
                   if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                      paddle_b_up()

                   if paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) < 10:
                      paddle_b_down()
        
    else:
      wn.update()