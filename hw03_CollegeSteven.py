#################################################################################
# Author: Steven Lintelman-Nader
# Username: CollegeSteven
#
# Assignment: Homework 3 - Main
# Purpose: Better understanding Git as a collaborative space.
# Google Doc Link: https://docs.google.com/document/d/15SLmGKKaDWuRTPArJhV6hO5h7I_5wTs5DAcg8XJPokU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


def cake(x, y, height, length):
    """
    Given a position near the top left of the cake, height and length, creates a cake or pink fortress with a turtle
    """

    # Create the initial top icing decoration.
    c = turtle.Turtle()
    c.hideturtle()
    c.teleport(x, y)
    c.speed(0)
    c.color("hot pink")
    c.begin_fill()
    c.right(315)
    for i in range(6):
        c.forward(length / 8.5)
        c.right(90)
        c.forward(length / 8.5)
        c.left(90)
    c.end_fill()

    # Create the main body of the cake
    c.color("pink")
    c.teleport(x, y)
    c.setheading(0)
    c.begin_fill()
    c.right(90)
    c.forward(height)
    c.left(90)
    c.forward(length)
    c.left(90)
    c.forward(height)
    c.end_fill()


def main():
    """
    Creates a triple decker cake with the message happy birthday on top
    """
    wn = turtle.Screen()
    for i in range(1, 4):
        cake((- 50 * i), (200 - (50 * i)), (50 * i), (100 * i))

    writing = turtle.Turtle()
    writing.hideturtle()
    writing.teleport(-145, 0)
    writing.write("HAPPY BIRTHDAY!!", font=("Comic Sans", 24, "bold"))
    wn.mainloop()


main()  # Starts the program!
