


#################################################################################
# Author: Sonam Tsering
# Username: Sonam
#
# Assignment:HW03
# Purpose:To draw a square and a circle.
# Google Doc Link:https://docs.google.com/document/d/1x2MMTAZWGlM-19RzjYo-OlmoP1kLayKSPCXF_cwvWYs/edit?usp=sharing
#
#################################################################################
# Acknowledgements://
#
#
#################################################################################

import turtle


def draw_square():
    """
    Draw a square using the turtle module.
    """
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.right(90)



def draw_circle():
    """
    Draws a circle using the turtle module.
    """
    t = turtle.Turtle()
    t.circle(100)
    # ...


def main():
    """
    Main function to demonstrate drawing shapes.
    """

    # Function calls to function_1 and function_2.
    draw_square()            # TODO  Remove when you replace it with your function
    draw_circle()            # TODO  Remove when you replace it with your function

if __name__ == "__main__":
    main()  # Starts the program!


