Considere: que tipo de avatar você quer criar? Um autorretrato? Algo no estilo Minecraft? Ou talvez algo completamente único?





Trabalhar com a função write()

Então, aqui está sua primeira tarefa: crie um avatar exclusivo, assine-o com a função write(), e adicione uma captura de tela ao seu cartão.

Antes de começar, vamos dar uma olhada nesta nova função.

A função write() nos permite adicionar texto aos nossos desenhos! Que texto? Isso é com você!

A função write() é muito similar à print(). Tudo o que você escrever entre colchetes será exibido na imagem.

A característica mais marcante da função write() são suas opções de personalização:

1. align – posicionamento do texto à esquerda, direita ou centro
t.write('Olá', align="esquerda")
t.write('Olá', align="direita")
t.write('Olá', align="centro")

2. font – configurações de fontes (tipo, tamanho, negrito)
t.write('Olá', font=('Arial', 8, 'normal'))



Aqui está a tarefa! 🧑‍💻

1. Selecione o tipo de avatar que você vai criar (você também pode criar algo completamente original)!

Variante #1 «Autorretrato»

Dê uma olhada no código que cria um autorretrato e personalize-o para se adequar a você! Você pode mudar o penteado ou adicionar acessórios adicionais! Você pode até usar chapéus! O WeCode não impõe limitações - expresse-se! Aqui estão alguns exemplos de avatares de autorretrato:

Screenshot-2022-10-28-at-12-32-22.png

Screenshot-2022-10-28-at-12-32-22.png

Variante #2 "Skin do Minecraft" (avançado)

Copie o código do modelo abaixo e adicione-o ao editor, depois exclua todo o resto. Altere as cores dos quadrados e adicione alguns novos elementos! Você também pode usar este site para encontrar algumas referências "em blocos"! 😎

O código do modelo para a variante #2:

import turtle
#variáveis ​​com cores
skin = 'green'
face = 'white'

t = turtle.Turtle()
t.speed(0)
t.shape("square")
t.color(skin)
t.pencolor("black")
t.up()
t.stamp()

t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.rt(90)
t.fd(20)
t.pencolor("black")
t.stamp()
t.rt(90)
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.fd(20)
t.stamp()
t.pencolor("black")
t.lt(90)
t.fd(20)
t.lt(90)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.rt(90)
t.fd(20)
t.rt(90)
t.stamp()
t.color(face)
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.color(skin)
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.color(face)
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.color(skin)
t.pencolor("black")
t.fd(20)
t.stamp()
t.lt(90)
t.fd(20)
t.lt(90)
t.pencolor("black")
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.rt(90)
t.fd(20)
t.rt(90)
t.color(skin)
t.pencolor("black")
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.lt(90)
t.fd(20)
t.lt(90)
t.pencolor("black")
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.color(face)
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.color(skin)
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.rt(90)
t.fd(20)
t.rt(90)
t.pencolor("black")
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()
t.pencolor("black")
t.fd(20)
t.stamp()

2. Se você escolheu a variante #1, finalize o código no editor.

Se você escolheu a variante #2, então copie o modelo acima no editor e então personalize o código. Sinta-se livre para alterar cores e adicionar novos elementos! Para adicionar novas cores ao seu avatar, você pode usar esta tabela de paleta de cores!

3. Assine seu avatar com a função write()

4. Faça uma captura de tela do seu avatar e envie para o chat!

Dicas 💡

Veja como fazer uma captura de tela

1. Windows - Se você tem um computador, pressione o botão "Print Screen". Se você tem um laptop, pressione dois botões simultaneamente: "Print Screen" e "Fn". Se você quiser tirar uma captura de tela somente da janela ativa (programa), pressione "Alt" e "Print Screen" simultaneamente no seu computador; "Alt" "Print Screen" e "Fn" no seu laptop.

2. MacOS - Para fazer uma captura de tela, pressione e segure as três teclas a seguir simultaneamente: Shift, Command e 3
