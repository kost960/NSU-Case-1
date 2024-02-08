import turtle
def rectangle(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)

def main_rectangle():
    rectangle(-200, 200,90, 180)
    turtle.done()

main_rectangle()