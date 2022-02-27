#step 4 
#angle method
import turtle

#define constants
#use capital letters
TRIANGLE = 3
SQUARE = 4
PENTAGON = 5
HEXAGON = 6
SEPTAGON = 7
OCTAGON = 8
NONAGON = 9

def draw_shape(sides, color):
   
   turtle.color(color)
   
   for i in range(0, sides):
       turtle.fd(50) 
       turtle.lt(360/sides)
   turtle.fd(140)
    
   
turtle.goto(-400,0)

draw_shape(TRIANGLE, "green")
draw_shape(SQUARE, "blue")
draw_shape(PENTAGON, "orange")
draw_shape(HEXAGON, "red")
draw_shape(SEPTAGON, "pink")
draw_shape(OCTAGON, "violet")
draw_shape(NONAGON, "dark green")

delay = input("Press enter to finish")