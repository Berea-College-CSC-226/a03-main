#################################################################################
# Author: michael
# Username: vargas
#
# Assignment: hw03
# Purpose: exploring how to use git
# Google Doc Link: https://docs.google.com/document/d/1N8o9ARVBX-O5GMWZkPOXhTASRz2FqRt-0w56s1F24e0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_heart(bob):
    bob.begin_fill()
    bob.penup()
    bob.color("red")
    bob.goto(0, -100)
    bob.pendown()
    bob.left(45)
    bob.forward(200)
    bob.circle(100, 200)
    bob.right(125)
    bob.circle(100, 200)
    bob.goto(0, -100)
    bob.end_fill()
    """
    Draws and fills heart
    """


def draw_h(bob):
    bob.begin_fill()
    bob.penup()
    bob.goto(-150, 100)
    bob.color("black")
    bob.pendown()
    bob.left(130)
    bob.forward(50)
    bob.right(180)
    bob.forward(25)
    bob.left(90)
    bob.forward(25)
    bob.left(90)
    bob.forward(25)
    bob.right(180)
    bob.forward(50)


def draw_a(bob):
    bob.penup()
    bob.left(100)
    bob.forward(25)
    bob.pendown()
    bob.left(60)
    bob.forward(50)
    bob.right(140)
    bob.forward(50)
    bob.right(180)
    bob.forward(25)
    bob.left(75)
    bob.forward(15)


def draw_p1(bob):
    bob.penup()
    bob.left(90)
    bob.forward(25)
    bob.left(90)
    bob.forward(40)
    bob.pendown()
    bob.left(85)
    bob.forward(45)
    bob.right(45)
    bob.circle(-15, 250)


def draw_p2(bob):
    bob.penup()
    bob.left(120)
    bob.forward(25)
    bob.left(90)
    bob.forward(40)
    bob.pendown()
    bob.left(85)
    bob.forward(45)
    bob.right(45)
    bob.circle(-15, 250)


def draw_y(bob):
    bob.penup()
    bob.left(120)
    bob.forward(25)
    bob.left(90)
    bob.forward(50)
    bob.pendown()
    bob.left(85)
    bob.forward(30)
    bob.left(35)
    bob.forward(25)
    bob.penup()
    bob.right(130)
    bob.forward(25)
    bob.right(115)
    bob.pendown()
    bob.forward(20)


def draw_v(bob):
    bob.penup()
    bob.goto(-150, 70)
    bob.left(50)
    bob.pendown()
    bob.forward(40)
    bob.left(140)
    bob.forward(40)



def draw_dash(bob):
    bob.penup()
    bob.goto(-110, 50)
    bob.pendown()
    bob.right(70)
    bob.forward(20)


def draw_d(bob):
    bob.penup()
    bob.goto(-80,50)
    bob.pendown()
    bob.left(90)
    bob.forward(20)
    bob.right(180)
    bob.forward(40)
    bob.left(50)
    bob.circle(25, 250)



def draw_a2(bob):
    bob.penup()
    bob.goto(-25, 25)
    bob.pendown()
    bob.right(140)
    bob.forward(50)
    bob.right(140)
    bob.forward(50)
    bob.right(180)
    bob.forward(25)
    bob.left(75)
    bob.forward(15)


def draw_y2(bob):
    bob.penup()
    bob.goto(35, 25)
    bob.right(95)
    bob.pendown()
    bob.forward(30)
    bob.left(35)
    bob.forward(25)
    bob.penup()
    bob.right(130)
    bob.forward(25)
    bob.right(115)
    bob.pendown()
    bob.forward(20)
    bob.penup()
    bob.goto(500, 500)

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.bgcolor('#1D7F19')

    bob = turtle.Turtle()
    bob.pensize(5)
    bob.speed(10)
    draw_heart(bob)
    draw_h(bob)
    draw_a(bob)
    draw_p1(bob)
    draw_p2(bob)
    draw_y(bob)
    draw_v(bob)
    draw_dash(bob)
    draw_d(bob)
    draw_a2(bob)
    draw_y2(bob)
    wn.exitonclick()


main()