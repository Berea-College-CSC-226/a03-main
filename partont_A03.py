# Tyler Parton
# partont_a03
# Google Doc Link- https://docs.google.com/document/d/1QPD0W7xIPh2vItGyULTXRGQNNttc85hhRq7L6U3FQG8/edit#

import turtle
wn = turtle.Screen()

def draw_house():
    """Begin Drawing Primary Shape"""
    slowpoke = turtle.Turtle()
    slowpoke.pensize(10)
    wn.bgcolor('#00008B')
    slowpoke.color('gray')

    for house in range(4):
        slowpoke.fd(170)
        slowpoke.right(90)
    slowpoke.right(90)
    slowpoke.fd(9)
    slowpoke.left(90)
    slowpoke.speed(0)

    ''' Filling in the Primary Shape'''

    for fill in range(9):
        slowpoke.fd(170)
        slowpoke.right(90)
        slowpoke.fd(9)
        slowpoke.right(90)
        slowpoke.fd(170)
        slowpoke.left(90)
        slowpoke.fd(9)
        slowpoke.left(90)
    slowpoke.fd(170)
    slowpoke.right(90)
    slowpoke.fd(3)
    slowpoke.right(90)
    slowpoke.fd(170)

    '''Creating Windows'''

    slowpoke.color('yellow')
    slowpoke.penup()
    slowpoke.setpos(-2,-9)
    slowpoke.left(180)
    slowpoke.penup()
    slowpoke.fd(15)

    for windows in range (4):
        slowpoke.pendown()
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.fd(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.penup()
        slowpoke.fd(45)
    # Have to get setup on new line which is why I break from Loop
    slowpoke.penup()
    slowpoke.right(90)
    slowpoke.forward(45)
    slowpoke.right(90)
    slowpoke.fd(35)
    # Starting second set of windows
    for windows in range (4):
        slowpoke.pendown()
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.fd(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.penup()
        slowpoke.fd(45)

    slowpoke.penup()
    slowpoke.left(90)
    slowpoke.forward(45)
    slowpoke.left(90)
    slowpoke.fd(35)

    for windows in range(4):
        slowpoke.pendown()
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.fd(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.penup()
        slowpoke.fd(45)

    slowpoke.penup()
    slowpoke.right(90)
    slowpoke.forward(45)
    slowpoke.right(90)
    slowpoke.fd(35)

    for windows in range(4):
        slowpoke.pendown()
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.fd(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.forward(10)
        slowpoke.right(90)
        slowpoke.penup()
        slowpoke.fd(45)

    slowpoke.penup()
    slowpoke.left(90)
    slowpoke.forward(45)
    slowpoke.left(90)
    slowpoke.color('green')
    slowpoke.forward(360)
    slowpoke.left(180)
    slowpoke.pensize(30)
    slowpoke.pendown()

    for grass in range(3):
        slowpoke.forward(670)
        slowpoke.left(90)
        slowpoke.forward(20)
        slowpoke.left(90)
        slowpoke.forward(670)
        slowpoke.right(90)
        slowpoke.forward(20)
        slowpoke.right(90)

    slowpoke.color('black')








def main():
    draw_house()



main()

wn.exitonclick()