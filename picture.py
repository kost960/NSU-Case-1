import turtle

turtle.screensize(1920, 1080)

def sky(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#7eccec')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)

    turtle.end_fill()
sky( -960, -80, 1920, 540 )

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

def ns_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()

ns_rckt(-840,450, 35)

def bd_rckt1(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#999999')
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

bd_rckt1(-815,421, 50)

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
    turtle.forward(a*(2**0.5))
    turtle.right(90)
    turtle.end_fill()

bd_rckt2 (-865, 415,69)

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
    turtle.forward(a*(2**0.5))
    turtle.right(45)
    turtle.end_fill()

bd_rckt3 (-815, 361,50)

def wingl_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#eeeeee')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5*a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5*a)
    turtle.right(30)
    turtle.end_fill()


wingl_rckt(-869, 335,25)

def wingr_rckt(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#eeeeee')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(1.5*a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(1.5*a)
    turtle.right(120)
    turtle.end_fill()

wingr_rckt(-811, 335,25)

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

fire_rckt(-840, 282,25)

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
    turtle.right(30)

fire_rckt2(-840, 262,25)

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

def head(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#fce5cd')
    turtle.begin_fill()
    for i in range (6):
        turtle.left(60)
        turtle.forward(a)
    turtle.end_fill()

head(-220, -175, 25)

def bd_hm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffffff')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

bd_hm(-250, -180,75)

def arm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#ffffff')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5*a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(1.5*a)
    turtle.right(30)
    turtle.end_fill()

arm(-253, -180,35)

def lgs_hm (x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#f1c232')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(45)
    turtle.end_fill()

lgs_hm(-220, -230,75)

def knee(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('#f1c232')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()

knee(-217, -275,45, 64)

def foot_r(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()

foot_r(-220, -320,24, 33)

def foot_l(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

foot_l(-310, -290,25)

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
    turtle.right(90)
    turtle.end_fill()

fish3ass( 823, -460, 15)


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
turtle.done()
