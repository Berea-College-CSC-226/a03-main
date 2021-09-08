#################################################################################
# Author: John Cox
# Username: coxj2
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learn more about Git
# Google Doc Link: https://docs.google.com/document/d/1T62Guh1IfBQMbXtI0dodMTa7tjEZ7ntFdILqF9CpXVw/edit?usp=sharing
#
#################################################################################

import turtle
import random

def drawRectangle(t, l, w):
    """
    Draw a Rectangle at current position with 't' turtle
    l = length, w = width
    """
    for i in range(2):
        t.fd(l)
        t.right(90)
        t.fd(w)
        t.right(90)
def drawSquare(t, l):
    """
    Draws a square at current position using 't' turtle with 'l' side length
    """
    drawRectangle(t, l, l)
def drawTriangle(t, x2, y2, x3, y3):
    """
    Draws a triangle starting from the turtles current position
    size and length depends on how far apart coordinates are
    (accepts a turtle name and two x, y coordinates)
    """
    startPoint = t.pos()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(startPoint)

def move(t, x, y):
    """
    Lifts pen and moves 't' turtle to specified x and y coordinates, then lowers the pen
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

def drawProceduralTriangles(t, x, y):
    """
    draw random sized triangles procedurally in a upside down V shape starting at the (x, y) coordinate with 't' turtle
    """
    move(t, x, y)
    goDown = False
    for i in range(8):
        drawTriangle(t, random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20), random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20))
        move(t, x, y)
        x += 80
        for j in range(2):
            drawTriangle(t, random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20), random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20))
            move(t, x, y)
            if y > 250:
                goDown = True
            if y < -250:
                goDown = False
            if goDown == True:
                y -= 80
            else:
                y += 80

def main():
    pencil = turtle.Turtle()
    wn = turtle.Screen()

    drawRectangle(pencil, 50, 25)
    move(pencil, 0, -50)
    drawTriangle(pencil, -50, -75, -90, -140)
    move(pencil, 0, 50)
    drawSquare(pencil, 40)
    drawProceduralTriangles(pencil, -280, -250)
    wn.exitonclick()


main()
