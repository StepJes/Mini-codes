from turtle import *
import coord

pen = Turtle()
bgcolor("#21252B")
pen.pensize(2)
pen.speed(0)
pen.penup()

def cuadrado():
    pen.pendown()
    pen.forward(15)
    pen.left(90)
    pen.forward(15)
    pen.left(90)
    pen.forward(15)
    pen.left(90)
    pen.forward(15)
    pen.left(90)
    pen.penup()


for x in range(len(coordenades.logo1)):
    pen.color("#4584b6")
    pen.goto(coordenades.logo1[x])
    cuadrado()


for x in range(len(coordenades.logo2)):
    pen.color("#ffde57")
    pen.goto(coordenades.logo1[x])
    cuadrado()



done()