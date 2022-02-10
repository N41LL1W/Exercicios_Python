def JogoAdvinhe():

    from random import randint
    from time import sleep
    computador = randint(0, 10) # Faz o computador escolher um número de 0 a 10
    acertou = False
    palpites = 0
    print('---===---'*6)
    print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
    print('---===---'*6)
    while not acertou:
        jogador = int(input('Em que número eu pensei? '))
        palpites += 1
        print('PROCESSANDO...')
        sleep(3)
        if jogador == computador:
            acertou = True
            print('PARABÉNS! Você conseguiu me vencer em {} palpite!'.format(palpites))
        else:
            if jogador < computador:
                print('Mais... Tente mais uma vez.')
            elif jogador > computador:
                print('Menos... Tente mais uma vez.')

JogoAdvinhe()