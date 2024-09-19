

#################################################################################
# Author: DieuMerci Nshizirungu
# Username: nshizirungud
#
# Assignment: HW03 Fully Functional Gitty
# Purpose:
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def show_coordinates(x, y):
    print(f"Coordinates: ({x}, {y})")


def draw_house(merci):
    merci.pendown()
    merci.color("orange")
    merci.begin_fill()
    merci.forward(300)
    merci.right(90)
    merci.forward(200)
    merci.right(90)
    merci.forward(300)
    merci.right(90)
    merci.forward(200)
    merci.end_fill()


def draw_roof(merci):
    merci.penup()
    merci.goto(5, 1)
    merci.pendown()
    merci.color("blue")
    merci.begin_fill()
    merci.right(45)
    merci.forward(100)
    merci.right(45)
    merci.forward(150)
    merci.right(45)
    merci.forward(100)
    merci.right(100)
    merci.end_fill()


def draw_chimney(merci):
    merci.color("red")
    merci.penup()
    merci.goto(120, 60)
    merci.pendown()
    merci.begin_fill()
    for i in range(4):
        merci.forward(60)
        merci.right(90)
    merci.end_fill()


def draw_window(merci, merci2):
    merci.penup()
    merci.color("lightblue")
    merci.goto(230, -50)
    merci.setheading(0)
    merci.pendown()
    merci.begin_fill()
    for i in range(4):
        merci.forward(60)
        merci.right(90)
    merci.end_fill()
    merci2.penup()
    merci2.color("lightblue")
    merci2.goto(7, -60)
    merci2.setheading(0)
    merci2.pendown()
    merci2.begin_fill()
    for i in range(4):
        merci2.forward(60)
        merci2.right(90)
    merci2.hideturtle()
    merci2.end_fill()


def draw_door(merci):
    merci.penup()
    merci.color("lightblue")
    merci.goto(136, -133)
    merci.setheading(0)
    merci.pendown()
    merci.begin_fill()
    for i in range(4):
        merci.forward(60)
        merci.right(90)
    merci.hideturtle()
    merci.end_fill()


def main():
    wn = turtle.Screen()
    wn.bgcolor("purple")
    merci = turtle.Turtle()
    merci2 = turtle.Turtle()

    draw_house(merci)
    draw_roof(merci)
    draw_chimney(merci)
    draw_window(merci, merci2)
    draw_door(merci)
    wn.onscreenclick(show_coordinates)
    turtle.mainloop()

    # merci.penup()
    merci.goto(300, 200)


main()