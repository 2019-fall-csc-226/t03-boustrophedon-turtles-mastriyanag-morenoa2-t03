#################################################################################
# Author:
# Username:
#
# Assignment:
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
import random # Imports the random library

def function_1(turtle, size):
    """
    Takes in the turtle and the size of the square in order
    to draw the fill of the square
    """
    turtle.pensize(20)
    turtle.speed(0)

    # Makes a random rgb val
    turtle.color(random.random(), random.random(), random.random())

    mySize = int(size/20)
    for i in range(0, mySize):
        if i > mySize-2:
            turtle.forward((20 * i)-20)
            turtle.left(90)
            break
        for k in range(0, 2):
            turtle.forward(20*i)
            turtle.left(90)

def function_2(size):
    """
    Takes in the size of the square to make the border of the square
    """
    square = turtle.Turtle()
    square.pensize(20)

    # Makes a random rgb val
    square.color(random.random(), random.random(), random.random())

    square.penup()
    for i in range(0, 2):
        square.forward(size/2)
        square.left(90)
    square.pendown()

    for i in range(0, 4):
        square.forward(size)
        square.left(90)

def main():
    """
    The whole sett-up. Here everything is called.
    """
    wn = turtle.Screen()
    ourTurtle = turtle.Turtle()
    size = 600

    # width is 90% of screen, height is 80% of screen. Screen appears at the center of screen
    wn.setup(width=0.9, height=0.9, startx=None, starty=None)

    ourTurtle.shape("turtle")

    function_2(size)  # Function call to function_2
    function_1(ourTurtle, size)            # Function call to function_1

    wn.exitonclick()

main()

