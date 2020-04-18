import turtle
import random
from turtle import *

anthony = turtle.Turtle()
anthony.speed(0)
anthony.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    anthony.setheading(90)
    anthony.forward(100)
    
def down():
    anthony.setheading(270)
    anthony.forward(100)

def left():
    anthony.setheading(180)
    anthony.forward(100)

def right():
    anthony.setheading(0)
    anthony.forward(100)

def clickleft(x, y):
    anthony.color(random.choice(colors))

def clickright(x, y):
    anthony.stamp()


turtle.listen()

# turtle.onclick(clickleft, 1)    #click on turtle
turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)


turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()