#################################################################################
# Author: Dawson Lakes
# Username: lakesd3
#
# Assignment: HW03
# Purpose: Draw a Person with colors using functions.
# Google Doc Link: https://docs.google.com/document/d/1ln0oyXvMbdzL3VVBTqcN4mgtV0iLCc3-Pke13agS4eo/edit?usp=sharing
#
#############################################################################

import turtle


wn = turtle.Screen()
wn.bgcolor("blue")


stickman = turtle.Turtle()
stickman.pensize(10)


def draw_square_head():
    stickman.penup()
    stickman.goto(-30, 100)
    stickman.pendown()
    stickman.fillcolor("lightblue")
    for _ in range(4):
        stickman.fd(60)
        stickman.left(90)



def draw_body():
    stickman.penup()
    stickman.goto(0, 100)
    stickman.pendown()
    stickman.setheading(-90)  # used turtle library for help with setheading, and .fd
    stickman.fd(100)



def draw_arms():
    stickman.penup()
    stickman.goto(0, 50)
    stickman.pendown()
    stickman.setheading(180)
    stickman.fd(50)

    stickman.penup()
    stickman.goto(0, 50)
    stickman.pendown()
    stickman.setheading(0)
    stickman.fd(50)


# draws the legs of the stickman
def draw_legs():
    stickman.penup()
    stickman.goto(0, 0)
    stickman.pendown()
    stickman.setheading(-45)
    stickman.fd(70)

    stickman.penup()
    stickman.goto(0, 0)
    stickman.pendown()
    stickman.setheading(-135) # sends the turtle to make the right leg
    stickman.fd(70)


def draw_balloon():
    stickman.penup()
    stickman.goto(50, 50)  # Position near the stickman's hand
    stickman.pendown()
    stickman.pensize(4)
    stickman.setheading(90)  # Move upwards
    stickman.fd(100)

    # Draw the balloon
    stickman.penup()
    stickman.goto(50, 150)
    stickman.pendown()
    stickman.fillcolor("red")
    stickman.begin_fill()
    stickman.circle(30)  # Draw a circle for the balloon
    stickman.end_fill()


def main():
    stickman.pencolor("black")
    draw_square_head()
    draw_body()
    draw_arms()
    draw_legs()
    draw_balloon()  # Draw the balloon after the stickman
    wn.exitonclick()



if __name__ == "__main__":
    main()
