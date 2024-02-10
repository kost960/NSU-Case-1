import turtle

def sqr_bd_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffbe69')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.end_fill()

sqr_bd_hm(-105, 120,200)


def wnd_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('lightblue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.end_fill()

wnd_hm(-75, 70,60)


def door_hm(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#382000')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.end_fill()

door_hm(10, -80,55, 110)


def trp_rf_hm (x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#9c3116')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(60)
    turtle.forward(c)
    turtle.left(60)
    turtle.forward(b)
    turtle.end_fill()

trp_rf_hm(-130, 120,250, 90, 160)


def tr_rf_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#9c3116')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()

tr_rf_hm(-5, 302,120)


def chim_hm(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#333232')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()

chim_hm(-85, 198,20, 60)


def smk_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#b5b5b5')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(a)
    turtle.end_fill()
    turtle.left(60)

smk_hm(-50, 297,45)

def grass(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)

    turtle.end_fill()
grass( -960, -80, 1920, 480 )

def legrab( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()

legrab( -840, -500, 30)


def legrab2( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()

legrab2( -840, -500, 45)

def bodyrab( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#D1BC8A')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()

bodyrab( -885, -500, 60)
def bodyrab2( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#D1BC8A')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()

bodyrab2( -825, -440, 60)

def armrab( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(90)
    turtle.end_fill()

armrab(-825, -425, 30)

def hatrab(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#D1BC8A')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


hatrab(-825, -365, 30)

def earsrab(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#FFB6C1')
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(1.5 * a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(1.5 * a)
    turtle.left(60)
    turtle.forward(a)
    turtle.end_fill()


earsrab(-810, -365, 30)

def lake(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#0000FF')
    turtle.begin_fill()
    turtle.circle(a)
    turtle.end_fill()

lake(850, -500, 70)

def fishbody(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#848482')
    turtle.begin_fill()
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.end_fill()
    turtle.right(45)


fishbody(860, -460, 15)

def fisharm( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#808080')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.end_fill()
    turtle.fillcolor('#808080')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.end_fill()
    turtle.left(45)


fisharm( 860, -460, 30)

def fishhat( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#c0c0c0')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(90)
    turtle.end_fill()

fishhat( 860, -445, 21)

def fischass(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#00ffff')
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(1.5 * a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(1.5 * a)
    turtle.left(60)
    turtle.forward(a)
    turtle.end_fill()

fischass(838, -460, 15)


def fish2ass( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#00ffff')
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.right(45)
    turtle.end_fill()

fish2ass( 838, -460, 15)

def fish3ass( x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#00ffff')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.end_fill()

fish3ass( 823, -460, 15)






turtle.done()

