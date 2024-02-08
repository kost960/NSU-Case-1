import turtle

def hexagon(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    for i in range (6):
        turtle.left(60)
        turtle.forward(a)

def main_hexagon():
    hexagon(200, -200,250)
    turtle.done()

main_hexagon()