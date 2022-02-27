# up pong
# by shaurocks
# python
import turtle
import winsound

wn = turtle.Screen()
wn.title("up pong by shaurocks")
wn.setup(width=500, height=700)
wn.bgcolor("black")
wn.tracer(0)

# SCORE
score = 0


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3


# Paddle
paddle= turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto( 0, -270)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.pencolor("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.pendown()
pen.write("score : 0 ", align="center", font=("courier", 24, "normal"))

# Fuction
def paddle_left():
        x = paddle.xcor()
        x -= 20
        paddle.setx(x)

def paddle_right():
        x = paddle.xcor()
        x += 20
        paddle.setx(x)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_right, "d")

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        
wn.listen()
wn.onkeypress(toggle_pause, "p") 

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
                score -= 1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
                pen.clear()
                pen.write("score : {} ".format(score), align="center", font=("courier", 24, "normal"))

            if ball.xcor()> 190:
                ball.setx(190)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            if ball.xcor()< -190:
                ball.setx(-190)
                ball.dx *= -1
                winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)

            # Paddle and ball collisions
            if ball.distance(paddle) < 20:
                    ball.sety(-250)
                    ball.dy *= -1
                    winsound.PlaySound("Pong_bounce.WAV", winsound.SND_ASYNC)
    
    else:
        wn.update()