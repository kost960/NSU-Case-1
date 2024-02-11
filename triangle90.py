import turtle

def triangle90(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.left(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)

triangle90(0, 0, 80)
turtle.done()
