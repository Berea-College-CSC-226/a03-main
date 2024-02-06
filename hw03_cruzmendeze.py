#####################################################################################
#
# Author: Eric Cruz-Mendez
# Username: cruzmendeze
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Google Doc Link: https://docs.google.com/document/d/1P5qvQ1eb9AhFPyGV7J0JwgZ8XdeqU9qpbF82LSsu6yM/edit?usp=sharing
#
#####################################################################################

import turtle
turtle.colormode(255)  # Set colormode to RGB value

# Function that makes the roof
def roof(shape):
    shape.color(255, 182, 193)  # RGB values for unnamed color
    shape.begin_fill()
    for side in range(3):       # Loop for triangular roof
        shape.forward(300)
        shape.left(120)
    shape.end_fill()  # Tells Python the shape is complete; now fill it
    shape.penup()

# Function that makes the main house rectangle
def house(shape):
    shape.color('pink')
    shape.pendown()
    for side in range(2):   # Makes the square shape for the house
        shape.forward(300)
        shape.right(90)
        shape.forward(250)
        shape.right(90)
    shape.end_fill()

# Function that make windows
def window(shape):
    shape.penup()
    shape.color('pink')
    for side in range(2):
        shape.forward(50)
        shape.right(90)
    for side in range(2):
        shape.pendown()
        shape.forward(-40)
        shape.right(90)
        shape.forward(-40)
        shape.right(90)
    shape.penup()
    shape.forward(-200)
    shape.right(90)
    shape.forward(-40)
    shape.pendown()
    for side in range(2):
        shape.forward(40)
        shape.right(90)
        shape.forward(-40)
        shape.right(90)
    shape.penup()
# Function that makes door
def door(shape):
    shape.color('pink')
    shape.forward(-160)
    shape.right(-90)
    shape.forward(120)
    shape.right(90)
    shape.pendown()
    shape.forward(80)
    shape.right(90)
    shape.forward(50)
    shape.right(90)
    shape.forward(80)
    shape.penup()

# Function that makes 'floor'
def floor(shape):
    shape.pendown()
    shape.right(90)
    shape.forward(-500)
    shape.forward(1500)
    shape.penup()
    shape.forward(-80)
# Function that makes flowers
def flowers(flower):
    flower = turtle.Turtle()
    flower.penup()
    flower.right(90)
    flower.forward(250)
    flower.right(90)
    flower.forward(250)
    flower.right(90)
    flower.pendown()
    flower.pencolor('blue')
    flower.forward(150)
    flower.shape("circle")

    for i in range(20, 80, 20):
        for r in range(10):
            for acolor in ["blue", "orange"]:
                flower.color(acolor)
                flower.left(24)
                flower.forward(i)
                id3 = flower.stamp()
                flower.backward(i)
    flower.penup()
    flower.right(180)
    flower.forward(150)
    flower.color("green")
    flower.clearstamp(id3)
    flower.right(90)
    flower.forward(175)
    flower.right(90)
    flower.pendown()

    flower.forward(150)
    for i in range(20, 80, 20):
        for r in range(10):
            for acolor in ["Green", "orange"]:
                flower.color(acolor)
                flower.left(24)
                flower.forward(i)
                id3 = flower.stamp()
                flower.backward(i)

def main():
    wn = turtle.Screen()
    wn.bgcolor("gray")
    shape = turtle.Turtle()
    shape.hideturtle()
    flower = turtle.Turtle()

    # Function calls to roof, house, window, door, floor, and flowers
    roof(shape)
    house(shape)
    window(shape)
    door(shape)
    floor(shape)
    flowers(flower)

    wn.exitonclick()

main()