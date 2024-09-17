
# Do not edit this file directly!
# Instead, create a new file called hw03_username.py and copy this code into it!

#################################################################################
# Author: Denys Zhytkov
# Username: zhytkovd
#
# Assignment: draw something complex, like a house, animal, or person.
# Purpose: A key learning goal for this homework is to practice creating functions
# Google Doc Link: https://docs.google.com/document/d/1tGnz7_R3oQGgibMZgD-vKZk6Lsckq5Xps91zl9ITcuE/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def rectangle(w,l,t):
    """
    function receives three parameters (width, length and turtle) and draws an appropriate rectangle
    """
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(l)
        t.right(90)


def background(t):
    """
    This function accepts turtle and draws a rectangle which I will use as a background for my drawing.
    """
    # moves turtle near top left corner
    t.up()
    t.goto(-300,300)
    t.down()

    # draws skies
    turtle.colormode(255)
    t.fillcolor((23,204,240)) # random color
    t.begin_fill()
    rectangle(700,500,t)
    t.end_fill()

    # draws green ground for house
    t.right(90)
    t.up()
    t.forward(250)
    t.down()
    t.left(90)
    t.fillcolor('light green')
    t.begin_fill()
    rectangle(700, 250, t)
    t.end_fill()

    #returns turtle to neutral position
    t.up()
    t.goto(0,0)
    t.down()


def window(x,y,t):
    """
    Accepts turtle and coordinates (x,y). Draws a window on the appropriate coordinates
    """

    # puts turtle on the correct spot
    t.up()
    t.goto(x,y)
    t.seth(0)
    t.down()

    # draws main window
    t.fillcolor('light blue')
    t.begin_fill()
    rectangle(70,100,t)
    t.end_fill()

    #draws frame of the window
    t.forward(35)
    t.color('black')
    t.right(90)
    t.forward(100)
    t.forward(-50)
    t.left(90)
    t.forward(35)
    t.left(180)
    t.forward(70)


def house(t):
    """
    Accepts turtle and draws house using functions from turtle module
    """
    #draws main frame of the house
    t.up()
    t.goto(-50, 200)
    t.down()
    t.fillcolor("beige")
    t.begin_fill()
    rectangle(400,300,t)
    t.end_fill()

    # draws a roof
    t.up()
    t.left(135)
    t.forward(50)
    t.down()
    t.right(135)
    t.fillcolor('brown')
    t.begin_fill()
    rectangle(450,50,t)
    t.end_fill()

    # draws a chimney
    t.up()
    t.right(45)
    t.forward(50)
    t.down()
    t.left(225)
    t.fillcolor('dark red')
    t.begin_fill()
    rectangle(20,60,t)
    t.end_fill()

    # draws three top windows
    for i in (0,130,260):
        window(i,150,t)

    # draws two down windows
    for i in (0,260):
        window(i,30,t)

    # draws door in the middle of the house
    t.up()
    t.goto(130,30)
    t.down()
    t.seth(0)
    t.fillcolor('brown')
    t.begin_fill()
    rectangle(70,130,t)
    t.end_fill()

    # draws the handle
    t.up()
    t.right(50)
    t.forward(90)
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(3)
    t.end_fill()


def flower(x,y,t):
    """
    Accepts turtle and coordinates (x,y). Draws a flower in the appropriate coordinates
    """
    # puts turtle on required coordinates
    t.up()
    t.goto(x,y)
    t.seth(0)
    t.down()

    t.left(90)
    t.forward(40)
    t.fillcolor('white')
    for i in range(5):
        #fills the center of the daisy during the last iteration
        if i == 4:
            t.fillcolor('yellow')
            t.begin_fill()
            t.circle(7)
            t.end_fill()
            break
        #draws four white circles for the flower
        t.fillcolor('white')
        t.begin_fill()
        t.circle(7)
        t.left(72)
        t.forward(3)
        t.end_fill()


def main():
    """
    Main() calls three functions to draw a picture using turtle module
    """
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.speed(10)

    background(alex) # draws background with earth and sky
    house(alex) # draws house

    # draws 15 flowers nearby house
    x = -200
    for i in range(15):
        flower(x, -150, alex)
        x += 40

    wn.exitonclick()


main()  # Starts the program!