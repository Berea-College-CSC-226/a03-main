# Author: Garrett Roe
# Username: roeg

# Google Docs link: https://docs.google.com/document/d/14AuMpOEGnVlrqMT4WlpWgYE8xwzCifW_yIVDstlKOiY/edit?usp=sharing

import turtle



def window_1(pixie):
    pixie.penup()
    pixie.left(180)
    pixie.forward(100)
    pixie.pendown()
    pixie.right(90)
    pixie.forward(25)
    pixie.right(90)
    pixie.fd(30)
    pixie.left(180)
    pixie.fd(30)
    pixie.right(90)
    pixie.fd(25)
    pixie.right(90)
    pixie.forward(15)
    pixie.right(90)
    pixie.fd(50)
    pixie.right(180)
    pixie.fd(50)
    pixie.right(90)
    pixie.fd(15)
    pixie.right(90)
    pixie.forward(50)
    pixie.right(90)
    pixie.forward(30)

def window_2(pixie):
    pixie.penup()
    pixie.right(180)
    pixie.fd(190)
    pixie.pendown()
    pixie.left(90)
    pixie.fd(25)
    pixie.left(90)
    pixie.fd(30)
    pixie.left(180)
    pixie.fd(30)
    pixie.left(90)
    pixie.fd(25)
    pixie.left(90)
    pixie.fd(15)
    pixie.left(90)
    pixie.fd(50)
    pixie.right(180)
    pixie.fd(50)
    pixie.left(90)
    pixie.fd(15)
    pixie.left(90)
    pixie.fd(50)
    pixie.left(90)
    pixie.fd(30)

def base(alex):
    alex.penup()
    alex.fd(115)
    alex.left(90)
    alex.fd(80)
    alex.pendown()
    alex.left(90)
    alex.fd(240)
    alex.left(90)
    alex.fd(120)
    alex.left(90)
    alex.fd(240)
    alex.left(90)
    alex.fd(120)

def roof(alex):
    alex.left(75)
    alex.fd(180)
    alex.right(75)
    alex.fd(25)
    alex.left(90)
    alex.fd(20)
    alex.left(90)
    alex.fd(20)
    alex.left(75)
    alex.fd(23)
    alex.left(180)
    alex.fd(100)
    alex.left(126)
    alex.fd(85)


def background(wn):
    wn.bgcolor("blue")

def main():
