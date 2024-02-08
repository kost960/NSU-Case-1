import turtle

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)

def main_square():
    square(-200, 200,180)
    turtle.done()

main_square()