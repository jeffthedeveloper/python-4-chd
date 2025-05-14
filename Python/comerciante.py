import random

# Criar cartões

dragon = 100
elf = 75
orc = 50
witch = 25


# Código do vendedor
yourscore = 0
dealer = 0
while (dealer < 3 and yourscore < 3):

    print('Pontuação - Jogador:', yourscore, 'Vendedor: - ', dealer)
    you = int(input('Escolher: 100, 75, 50, 25'))
    if (you == dragon or you == elf or you == orc or you == witch):
        comp = random.randint(1, 4)
        if comp == 1:
            comp = 100
        if comp == 2:
            comp = 75
        if comp == 3:
            comp = 50
        if comp == 4:
            comp = 25
        print('O vendedor escolheu: ', comp)
        if comp == you:
            print("EMPATE!")
        elif ((you == 100 and comp == 75) or
              (you == 100 and comp == 50) or
              (you == 100 and comp == 25) or
              (you == 50 and comp == 25) or
              (you == 75 and comp == 50) or
                (you == 75 and comp == 25)):
            print("Você venceu!")
            yourscore += 1
        else:
            print('Você perdeu')
            dealer += 1
    else:
        print('Não existe essa opção')
if yourscore > dealer:
    print("Você venceu, e aqui está sua dica:")
    print("Equipe 1 - use operadores aritméticos e exemplos para sobrecarregar, bem como multiplicar palavras para sobrecarregar, use print()")
    print("Equipe 2 - use a função print() para emitir a mensagem de contagem regressiva, progresso e destruição")
