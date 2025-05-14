import turtle


def mhair(color):
    t.up()
    t.color(color)
    t.goto(100, 150)
    t.dot(30)
    t.goto(140, 130)
    t.dot(20)
    t.goto(60, 130)
    t.dot(20)
    t.ht()


def whair(color):
    t.up()
    t.color(color)
    t.goto(100, 150)
    t.dot(30)
    t.goto(140, 130)
    t.dot(20)
    t.goto(60, 130)
    t.dot(20)
    t.goto(40, 100)
    t.dot(20)
    t.goto(160, 100)
    t.dot(20)


t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.shape("turtle")
t.goto(200, 0)
t.goto(200, 200)
t.goto(0, 200)
t.goto(0, 0)
t.up()
t.goto(100, 100)
skin = '#ffdfc4'
nose = '#ffae6a'
# fundo
t.color('lightblue')
t.dot(100)
# cor da pele
t.color(skin)
t.dot(50)
# ouvidos
t.goto(50, 100)
t.dot(10)
t.goto(150, 100)
t.dot(10)
# olhos
t.color('white')
t.goto(75, 105)
t.dot(10)
t.goto(125, 105)
t.dot(10)
t.color('brown')
t.goto(75, 105)
t.dot(5)
t.goto(125, 105)
t.dot(5)
# nariz
t.color(nose)
t.goto(100, 90)
t.dot(5)
# boca
t.goto(110, 75)
t.color('black')
t.down()
t.goto(90, 75)
# cabelo
mhair('black')
# escreva seu código abaixo
