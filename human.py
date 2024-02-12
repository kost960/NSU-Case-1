import turtle

turtle.screensize(1920, 1080)


def bd_сhkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#444444')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


bd_сhkn(270, -180, 75)


def foot_chkn(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#444444')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()

foot_chkn(322, -207, 34, 48)


def tl_chkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffffff')
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


tl_chkn(265, -140, 75)


def tl2_chkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffffff')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()


tl2_chkn(228, -100, 52)

def tl3_chkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffffff')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(1.5*a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(1.5*a)
    turtle.right(135)
    turtle.forward(a)
    turtle.left(45)
    turtle.end_fill()

tl3_chkn(215, -170, 35)


def hd1_chkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#444444')
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


hd1_chkn(310, -141, 35)


def hd2_chkn(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()


hd2_chkn(334, -112, 35)


def ns_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()


ns_rckt(-840, 450, 35)


def bd_rckt1(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#999999')
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


bd_rckt1(-815, 421, 50)


def bd_rckt2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#5b5b5b')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(90)
    turtle.end_fill()


bd_rckt2(-865, 415, 69)


def bd_rckt3(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#999999')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(45)
    turtle.end_fill()


bd_rckt3(-815, 361, 50)


def wingl_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#eeeeee')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5 * a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5 * a)
    turtle.right(30)
    turtle.end_fill()


wingl_rckt(-869, 335, 25)


def wingr_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#eeeeee')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(1.5 * a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(1.5 * a)
    turtle.right(120)
    turtle.end_fill()


wingr_rckt(-811, 335, 25)


def fire_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.end_fill()


fire_rckt(-840, 282, 25)


def fire_rckt2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.end_fill()
    turtle.left(60)


fire_rckt2(-840, 262, 25)


def head(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    for i in range(6):
        turtle.left(60)
        turtle.forward(a)


head(-220, -175, 25)


def bd_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)


bd_hm(-250, -180, 75)


def parallelogram(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5 * a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5 * a)
    turtle.right(30)


parallelogram(-253, -180, 35)


def lgs_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(45)


lgs_hm(-220, -230, 75)


def knee(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(135)


knee(-217, -275, 45, 64)


def foot_r(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)


foot_r(-220, -320, 24, 33)


def foot_l(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * (2 ** 0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)


foot_l(-310, -290, 25)

turtle.done()
turtle.done()
