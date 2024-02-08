import turtle

def rhombus(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.left(60)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)

def main_rhombus():
    rhombus(-200, -200,180)
    turtle.done()

main_rhombus()