import turtle

def triangle(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)

def main_triangle():
    triangle(-200, 200,180)
    turtle.done()

main_triangle()