#Name: Dylan C. Ben
#Username: bend
#Repo link
#Google doc link: https://docs.google.com/document/d/1pWelrF7tgJuJ5la_QDR3w8rMjc3w9Y24Q7IWuv8Yugo/edit?usp=sharing

import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("Dark blue")


# Create a function to draw a rectangle
def draw_rectangle(color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


# Create a function to draw a triangle
def draw_triangle(color, size):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


# Draw the house
t.penup()
t.goto(-100, -100)
t.pendown()
draw_rectangle("#9C2A58", 200, 150)

# Draw the door
t.penup()
t.goto(0, -100)
t.pendown()
draw_rectangle("red", 40, 100)

# Draw the windows
t.penup()
t.goto(-60, -10)
t.pendown()
draw_rectangle("#F5FDFA", 40, 40)

t.penup()
t.goto(50, -10)
t.pendown()
draw_rectangle("#F5FDFA", 40, 40)

# Draw the roof
t.penup()
t.goto(-120, 50)
t.pendown()
draw_triangle("red", 240)

# Draw the tree
t.penup()
t.goto(160, -40)
t.pendown()
draw_triangle("green", 50)

t.penup()
t.goto(175, -40)
t.pendown()
draw_rectangle("brown", 20, -60)


# Draw the chimney
t.penup()
t.goto(50, 120)
t.pendown()
draw_rectangle("gray", 20, 50)

# The text for code
turtle.write("Dylan Marvelous House", True, align= "left")
turtle.write((), True)


# Close the drawing window on click
wn.exitonclick()
