import turtle
t = turtle.Turtle()
t.shape("turtle")

# defina a velocidade como zero aqui
t.speed(0)

# a tartaruga desenha a primeira linha
t.forward(100)
# diminua a velocidade da tartaruga aqui
t.speed(1)

# defina a espessura para 10 pixels
t.width(10)

# a tartaruga desenha a segunda linha
t.up()
t.goto(0, -50)
t.down()
t.forward(100)
