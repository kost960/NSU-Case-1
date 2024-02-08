import turtle

def trapezoid (x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(60)
    turtle.forward(c)
    turtle.left(60)
    turtle.forward(b)

def main_trapezoid():
    trapezoid(-200, 200,250, 90, 160)
    turtle.done()

main_trapezoid()