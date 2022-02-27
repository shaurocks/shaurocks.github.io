# Snake game
# by Shaurocks
# python

import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0
top_score = 400

border = turtle.Turtle()
border.penup()
border.pencolor("white")
border.pensize("5")
border.goto(-290, 290)
border.pendown()
border.forward(580)
border.right(90)
border.forward(580)
border.right(90)
border.forward(580)
border.right(90)
border.forward(580)
border.right(90)
border.penup()
border.hideturtle()

# screen setup
wn = turtle.Screen()
wn.title("Snake game by Shaurocks")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)# Turns off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)

# snake virus
virus = turtle.Turtle()
virus.speed(0)
virus.shape("triangle")
virus.color("light green")
virus.penup()
virus.goto(0,240)

# turtle 
Turtle = turtle.Turtle()
Turtle.speed(0)
Turtle.shape("turtle")
Turtle.color("pink")
Turtle.penup()
Turtle.goto(10000, 10000)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score : 0 High Score : 0 Top Score: 400", align="center", font=("courier", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -330)
pen2.write("Use 'wsad' to move. Do'nt eat triangle or yourself or border. Surpass top score to eat turtle.", align="center", font=("courier", 15, "italic"))


# functions
def go_up():
    if head.direction != "down":
       head.direction = "up"

def go_down():
    if head.direction != "up":   
       head.direction = "down"

def go_left():
    if head.direction != "right":
       head.direction = "left"

def go_right():
    if head.direction != "left":
       head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        
wn.listen()
wn.onkeypress(toggle_pause, "p")

# Keyboard Binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop
while True:
    wn.update()

    #Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        #Reset delay
        delay = 0.1
        time.sleep(1)
        head.setposition(0, 0)
        head.direction = "stop"
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {} Top score: {}".format(score, high_score, top_score), align="center", font=("Courier", 24, "normal"))
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.setposition(1000, 1000)

        #clear segments list
        segments.clear()

    #check for collision with food
    if head.distance(food) < 20:
        #move food to an random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.setposition(x, y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten delay
        delay -= 0.001

        #Increase the score
        score += 10
        
        if score > high_score:
            high_score = score

        if top_score < score:
            top_score += 400
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            Turtle.setposition(x, y)
            Turtle.showturtle()
  
        pen.clear()
        pen.write("Score: {} High Score: {} Top score: {}".format(score, high_score, top_score), align="center", font=("Courier", 24, "normal"))

    #check for collision with turtle
    if head.distance(Turtle) < 20:
        #move Turtle to position
        Turtle.setposition(1000, 1000)
        Turtle.hideturtle()

        #remove a segment
        for segment in segments:
            segment.setposition(1000, 1000)

        #clear segments list
        segments.clear()

        #Shorten delay
        delay -= 0.001
    
        pen.clear()
        pen.write("Score: {} High Score: {} Top score: {}".format(score, high_score, top_score), align="center", font=("Courier", 24, "normal"))

    #check for collision with virus
    if head.distance(virus) < 20:
        #move virus to an random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        virus.setposition(x, y)

        last_segment = segments[-1]
        last_segment.goto(1000, 1000) # Move segment off screen
        segments.remove(last_segment)

        #reset delay
        delay += 0.05

        #decrease the score
        score -= 50
            
        pen.clear()
        pen.write("Score: {} High Score: {} Top score: {}".format(score, high_score, top_score), align="center", font=("Courier", 24, "normal"))       

    #move end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].setposition(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].setposition(x, y)
                           
    move()

    #check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            #Reset delay
            delay = 0.01
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            pen.clear()
            score = 0
            pen.write("Score: {} High Score: {} Top score: {}".format(score, high_score, top_score), align="center", font=("Courier", 24, "normal"))
            head.direction = "stop"

            #hide the segments
            for segment in segments:
                segment.setposition(1000, 1000)

            #clear segments list
            segments.clear()
            
    time.sleep(delay)

#wn.mainloop()
