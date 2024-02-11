import turtle

def lake(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#0000FF')
    turtle.begin_fill()
    turtle.circle(a)
    turtle.end_fill()

lake(850, -500, 70)



def boatbelow(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#964B00')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()
    turtle.left(45)

boatbelow(850, -410, 15)



def boatbelow2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#964B00')
    turtle.begin_fill()
    turtle.left(135)
    turtle.forward(1.5 * a)
    turtle.left(45)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(1.5 * a)
    turtle.left(45)
    turtle.forward(a)
    turtle.end_fill()

boatbelow2(850, -410, 10)


def boatmid(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#654321')
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
    turtle.left(45)

boatmid(861, -399, 10)

def boatmid2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#654321')
    turtle.begin_fill()
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.end_fill()

boatmid2(861, -399, 10)




def boatup(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ECEBE9')
    turtle.begin_fill()
    turtle.left(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()



boatup(861, -385, 20)


def boatup2( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#FF0000')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()


boatup2( 847, -370, 10)

def boatmid3( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#d3d3d3')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()

boatmid3( 847, -395, 20)


turtle.done()