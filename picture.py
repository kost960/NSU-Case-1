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

smk_hm(-50, 297,45)
turtle.done()

