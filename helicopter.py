import turtle

def blade1(x,y,a):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.fillcolor('#d3d3d3')
    turtle.begin_fill()
    turtle.forward(1.5*a)
    turtle.left(45)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(1.5*a)
    turtle.left(45)
    turtle.forward(a)
    turtle.left(135)
    turtle.end_fill()

blade1(840,450, 25)

def blade2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#d3d3d3')
    turtle.begin_fill()
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.end_fill()

blade2(840,450, 35)

def hlptrmid(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ECEBE9')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.end_fill()
    turtle.left(135)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(90)
    turtle.end_fill()

hlptrmid(840,450, 60)

def tail1(x, y, a):

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#c0c0c0')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.end_fill()
    turtle.left(135)
    turtle.fillcolor('#808080')
    turtle.begin_fill()
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()

tail1(797, 407, 25)

def tail2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#808000')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.end_fill()
    turtle.right(45)

tail2(751, 396, 30)


turtle.done()




