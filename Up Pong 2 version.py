# up pong 2 version
# by shaurocks
# python
import turtle
import winsound

wn = turtle.Screen()
wn.title("up pong 2 by shaurocks")
wn.setup(width=500, height=700)
wn.bgcolor("white")
wn.tracer(0)

# SCORE
Ai = 0
AiTwo = 0

# boundary
b = turtle.Turtle()
b.penup()
b.pencolor("black")
b.pensize("5")
b.goto(-210, 290)
b.pendown()
b.forward(420)
b.right(90)
b.forward(580)
b.right(90)
b.forward(420)
b.right(90)
b.forward(580)
b.hideturtle()

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("blue")
ball2.penup()
ball2.goto(0,0)
ball2.dx = -0.5
ball2.dy = 0.5

# Paddle
paddle= turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("black")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto( 0, -270)

# Paddle2
paddle2= turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=1, stretch_len=5)
paddle2.penup()
paddle2.goto( 0, -270)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.pencolor("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.pendown()
pen.write("AI 1 : 0   AI 2 : 0 ", align="center", font=("courier", 24, "normal"))

# pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.pencolor("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(-450, 300)
pen2.pendown()
pen2.write("press key p to toggle pause", align="center", font=("courier", 10, "normal"))

# pen3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.pencolor("blue")
pen3.penup()
pen3.hideturtle()
pen3.goto(-450, 200)
pen3.pendown()
pen3.write("press key 1 to turn off Ai 1 or key 2 to turn off Ai 2 ", align="center", font=("courier", 10, "normal"))

# pen4
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.pencolor("black")
pen4.penup()
pen4.hideturtle()
pen4.goto(-450, 100)
pen4.pendown()
pen4.write("use w,s to move for Ai 1", align="center", font=("courier", 10, "normal"))

# pen5
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.pencolor("blue")
pen5.penup()
pen5.hideturtle()
pen5.goto(-450, 0)
pen5.pendown()
pen5.write("use right,left arrow to move for Ai 2 ", align="center", font=("courier", 10, "normal"))

# Fuction
def paddle_left():
        x = paddle.xcor()
        x -= 20
        paddle.setx(x)

def paddle_right():
        x = paddle.xcor()
        x += 20
        paddle.setx(x)


def paddle2_left():
        x = paddle2.xcor()
        x -= 20
        paddle2.setx(x)

def paddle2_right():
        x = paddle2.xcor()
        x += 20
        paddle2.setx(x)



# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_right, "d")
wn.onkeypress(paddle2_left, "Left")
wn.onkeypress(paddle2_right, "Right")

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
is_Ai1 = False

def toggle_ai():
    global is_Ai
    if is_Ai == True:
        is_Ai = False
    else:
        is_Ai = True       
        
def toggle_ai1():
    global is_Ai1
    if is_Ai1 == True:
        is_Ai1 = False
    else:
        is_Ai1 = True       

wn.listen()
wn.onkeypress(toggle_ai, "2")
wn.onkeypress(toggle_ai1, "1")

while True:
    if not is_paused:
            wn.update()
            # move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            ball2.setx(ball2.xcor() + ball2.dx)
            ball2.sety(ball2.ycor() + ball2.dy)

            # Border Checking
            if ball.ycor()> 290:
                ball.sety(290)
                ball.dy *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball.ycor()< -290:
                ball.sety(-290)
                ball.dy *= -1
                Ai -= 1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
                pen.clear()
                pen.write("Ai : {}  Ai 2 : {}".format(Ai, AiTwo), align="center", font=("courier", 24, "normal"))

            if ball.xcor()> 190:
                ball.setx(190)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball.xcor()< -190:
                ball.setx(-190)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball2.ycor()> 290:
                ball2.sety(290)
                ball2.dy *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball2.ycor()< -290:
                ball2.sety(-290)
                ball2.dy *= -1
                AiTwo -= 1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
                pen.clear()
                pen.write("Ai : {} Ai 2 : {} ".format(Ai, AiTwo), align="center", font=("courier", 24, "normal"))

            if ball2.xcor()> 190:
                ball2.setx(190)
                ball2.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball2.xcor()< -190:
                ball2.setx(-190)
                ball2.dx *= -1     
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            # Paddle and border collision
            if paddle.xcor()> 170:
                paddle.setx(170)
            if paddle.xcor()< -170:
                paddle.setx(-170)
            if paddle2.xcor()> 170:
                paddle2.setx(170)
            if paddle2.xcor()< -170:
                paddle2.setx(-170)

            # Paddle and ball collisions
            if ball.distance(paddle) < 20:
                    ball.sety(-250)
                    ball.dy *= -1
                    winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball2.distance(paddle2) < 20:
                    ball2.sety(-250)
                    ball2.dy *= -1
                    winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
            
            # AI player
            if not is_Ai1:
                    if paddle.xcor() < ball.xcor() and abs(paddle.xcor() - ball.xcor()) > 10:
                       paddle_right()

                    if paddle.xcor() > ball.xcor() and abs(paddle.xcor() - ball.xcor()) < 10:
                       paddle_left()
             
            
            if not is_Ai:
                    if paddle2.xcor() < ball2.xcor() and abs(paddle2.xcor() - ball2.xcor()) > 10:
                       paddle2_right()

                    if paddle2.xcor() > ball2.xcor() and abs(paddle2.xcor() - ball2.xcor()) < 10:
                       paddle2_left()
                    

    
    else:
        wn.update()