
#

#################################################################################
# Author: Jacob Lewis
# Username: Lewisj6
#
# Assignment: HW03
# Purpose: To make a drawing of a cat
# Google Doc Link:https://docs.google.com/document/d/15UE6qjrHiqWdQAq-kwvJLQ1PeC6VtDp3PUm_LRi6t9Y/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# PythonIndex.com for helpful tutorials. As well as my roommate for helping me.
#
#################################################################################


import turtle
import math

window = turtle.Screen()
window.bgcolor('gray')

tess=turtle.Turtle()
tess.shape('turtle')
tess.color('green')
tess.speed(3)
tess.pensize(10)

"""
  Following definitions are required to make things easier to draw.
  """
def movePen(tess, x, y):
    tess.penup()
    tess.setposition(x, y)
    tess.pendown()



def movePenX(tess, x,):
    tess.penup()
    tess.setx(x)
    tess.pendown()

def movePenY(tess, y):
    tess.penup()
    tess.sety(y)
    tess.pendown()


def posAlongCircle(x,y,radius,angle):
    radians = math.radians(angle)
    return [x+(radius*math.sin(radians))
                ,y+(radius*math.cos(radians))]


def main():
    """
    Draws a cat
    """

    # Function calls to movePenY and function_2.

    movePenY(tess,-150)
    tess.circle(150)

    movePenY(tess, -20+-15)
    tess.circle(20)

    movePen(tess,-100,-20+-15)
    tess.right(90)
    tess.circle(50, 180)
    tess.left(180)
    tess.circle(50,180)

    movePen(tess,30, 40,)
    tess.right(180)
    tess.circle(30, 180)

    movePen(tess, -30, 40)
    tess.circle(30, -180)

    movePen(tess,-20, -60+-15)
    tess.circle(20,180)

    movePen(tess, 50, -15)
    tess.setheading(0)
    tess.forward(180)

    movePen(tess, 50, 0)
    tess.left(5)
    tess.forward(180)

    movePen(tess, -50,-15)
    tess.setheading(180)
    tess.forward(180)
    movePen(tess, -50, 0)
    tess.left(-5)
    tess.forward(180)

    earBeginAngle = 25
    earsize = 85
    earWidth = 22
    PostionA = posAlongCircle(0, 0, 150, earBeginAngle)
    movePen(tess, PostionA[0], PostionA[1])

    positionB = posAlongCircle(0, 0, 150 + earsize, earBeginAngle + earWidth )
    tess.setposition(positionB[0], positionB[1])

    positionC = posAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
    tess.setposition(positionC[0], positionC[1])

    PositionA = posAlongCircle(0, 0, 150, -earBeginAngle)
    movePen(tess, PositionA[0], PositionA[1])
    positionB = posAlongCircle(0, 0, 150 + earsize, -earBeginAngle + -earWidth)
    tess.setposition(positionB[0], positionB[1])
    positionC = posAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
    tess.setposition(positionC[0], positionC[1])





main()  # Starts the program!

