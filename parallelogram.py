import turtle

def parallelogram(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.left(120)
    turtle.forward(1.5*a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(1.5*a)
    turtle.left(60)
    turtle.forward(a)

parallelogram(-200, 200,180)
