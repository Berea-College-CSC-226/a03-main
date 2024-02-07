#################################################################################
# Author: Sonam Tsering
# Username: Sonam
#
# Assignment:HW03
# Purpose:Sonam's House
# Google Doc Link:https://docs.google.com/document/d/1x2MMTAZWGlM-19RzjYo-OlmoP1kLayKSPCXF_cwvWYs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#





import turtle

# Function to draw a house
def draw_house():
    # Create a turtle object
    my_turtle = turtle.Turtle()

    # Set background color
    turtle.bgcolor("lightblue")  # Changing background color to light blue

    # Draw the main body of the house
    my_turtle.penup()
    my_turtle.goto(-50, -50)
    my_turtle.pendown()
    my_turtle.color("brown")
    my_turtle.begin_fill()
    my_turtle.goto(-50, 50)
    my_turtle.goto(50, 50)
    my_turtle.goto(50, -50)
    my_turtle.goto(-50, -50)
    my_turtle.end_fill()

    # Draw the roof of the house
    my_turtle.penup()
    my_turtle.goto(-50, 50)
    my_turtle.pendown()
    my_turtle.color("red")
    my_turtle.begin_fill()
    my_turtle.goto(0, 100)
    my_turtle.goto(50, 50)
    my_turtle.end_fill()

    # Draw the door of the house
    my_turtle.penup()
    my_turtle.goto(-20, -50)
    my_turtle.pendown()
    my_turtle.color("blue")
    my_turtle.begin_fill()
    my_turtle.goto(-20, 0)
    my_turtle.goto(20, 0)
    my_turtle.goto(20, -50)
    my_turtle.goto(-20, -50)
    my_turtle.end_fill()

    # Draw a window on the house
    my_turtle.penup()
    my_turtle.goto(-40, 20)
    my_turtle.pendown()
    my_turtle.color("yellow")
    my_turtle.begin_fill()
    for _ in range(4):
        my_turtle.forward(20)
        my_turtle.left(90)
    my_turtle.end_fill()

    # Hide the turtle
    my_turtle.hideturtle()

    # Keep the window open
    turtle.done()

# Main function
def main():
    # Draw the house
    draw_house()

# Call the main function
main()
