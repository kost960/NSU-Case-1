import turtle

def pentagon(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    for i in range (5):
        turtle.left(72)
        turtle.forward(a)

def main_pentagon():
    pentagon(200, -200,250)
    turtle.done()

main_pentagon()