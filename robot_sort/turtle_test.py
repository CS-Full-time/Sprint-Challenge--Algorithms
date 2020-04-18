import random
import turtle

tim = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# shape and speed
tim.shape('turtle')
tim.speed(9)

# set color for the turtle
tim.color('red', 'blue')

# set pen width
tim.width(5)

# fill in shape with color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.fd(150)
tim.pendown()

tim.color('yellow', 'black')

tim.begin_fill()
for i in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()

a = 0

for x in range(250):
    randSpeed = random.randrange(0, 9)
    randColor = random.randrange(0, len(colors))
    randColor2 = random.randrange(0, len(colors))
    tim.color(colors[randColor], colors[randColor2])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    # tim.speed(randSpeed)
    tim.speed(0)
    tim.penup()
    # tim.setpos((rand1, rand2))
    tim.setpos((0, (-500 + a)))
    tim.pendown()
    tim.begin_fill()
    # tim.circle(random.randrange(0, 500))
    tim.circle(500 - a)
    tim.end_fill()
    tim.right(1)
    a += 2

turtle.mainloop()
