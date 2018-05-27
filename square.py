#!/usr/bin/python

import turtle

#new Turtle object
wn = turtle.Screen()
wn.title("Shapes")

#craete a square object
square = turtle.Turtle()
square.color("green")
square.pensize(1)

#craete a rectangle object
rectangle = turtle.Turtle()
rectangle.color("red")
rectangle.pensize(3)

#exercise: draw a square
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)

rectangle.penup() #list the pen from the canvas
rectangle.forward(100) #move the pen forward
rectangle.pendown() #place the pen down for writing

#exercise: draw a rectangle
rectangle.forward(100)
rectangle.right(90)
rectangle.forward(50)
rectangle.right(90)
rectangle.forward(100)
rectangle.right(90)
rectangle.forward(50)


turtle.exitonclick() #makes the shell exit on click

