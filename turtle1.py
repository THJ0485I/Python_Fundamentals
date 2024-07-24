import turtle
import random

#Settings
turtle.shape("turtle")
turtle.speed("normal")
turtle.Screen().colormode(255)

numCircles = int(input("Enter number of circles"))
radius = 40
startPos_x = -300
startPos_y = 200

turtle.penup()
turtle.goto(startPos_x, startPos_y)
turtle.pendown()

for TrainerEros in range(5):
    # Draw 1 row
    for i in range(numCircles):
        #draw and fill a circle
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.color(r, g, b)
        turtle.begin_fill()
        turtle.circle(radius, 360)
        turtle.end_fill()

        #Move to a new position
        turtle.penup()
        turtle.forward(radius * 2)
        turtle.pendown()

    # Move to the next row
    startPos_y = startPos_y - (radius * 2)
    turtle.penup()
    turtle.goto(startPos_x, startPos_y)
    turtle.pendown()


turtle.mainloop()