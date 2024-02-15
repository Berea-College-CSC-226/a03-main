


#################################################################################
# Author: Ricardo Bahena
# Username: Rica
#
# Assignment: homework 3
# Purpose: Buildng a house with a tree on the left side
# Google Doc Link: https://docs.google.com/document/d/1yAKz379Sjhg7QhFZoLcn1pLcg9lehsnHS3vDrVSa9Vo/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def house(dog):
    """
    this is the function house and it's cretaing a house with one window in the tope left
    """
    dog.left(90)
    dog.forward(250)
    dog.right(90)
    dog.forward(150)
    dog.right(90)
    dog.forward(250)
    dog.right(90)
    dog.forward(150)
    dog.penup()
    dog.right(90)
    dog.forward(150)
    dog.pendown()
    dog.forward(50)
    dog.right(90)
    dog.forward(50)
    dog.right(90)
    dog.forward(50)
    dog.right(90)
    dog.forward(50)
    dog.right(90)
    dog.penup()
    dog.forward(25)
    dog.pendown()
    dog.right(90)
    dog.forward(50)
    dog.right(90)
    dog.forward(25)
    dog.right(90)
    dog.forward(25)
    dog.right(90)
    dog.forward(50)

def door(dog):
    """
    this is the fucntion of the door where it's being created in the bottom right
    """
    dog.penup()
    dog.goto(0,0)
    dog.right(90)
    dog.forward(100)
    dog.pendown()
    dog.left(90)
    dog.forward(40)
    dog.right(90)
    dog.forward(50)
    dog.right(90)
    dog.forward(40)
    dog.right(90)
    dog.forward(25)
    dog.right(90)
    dog.forward(40)






def tree(dog):
    """
    this is the function where a tree is being created on the left side of the house
    """
    dog.penup()
    dog.goto(-150,0)
    dog.pendown()
    dog.forward(40)
    dog.penup()
    dog.goto(-180,0)
    dog.pendown()
    dog.forward(40)
    dog.right(45)
    dog.forward(23)
    dog.right(90)
    dog.forward(25)
    dog.right(135)
    dog.forward(40)
    dog.penup()
    dog.goto(-150, 0)
    dog.pendown()
    dog.forward(40)



def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """

    # Function calls to function_1 and function_2.
    screen= turtle.Screen()
    screen.bgcolor("lightblue")
    dog = turtle.Turtle()

    house(dog)
    door(dog)
    tree(dog)
    screen.exitonclick()


main()  # Starts the program!


