def Par_Impar():

    from random import randint

    while True:
        jogador = int(input('Diga um valor: '))
        computador = randint(0, 10)
        total = jogador + computador
        tipo = ' '
        v = 0
        while tipo not in 'PpIi':
            tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
        print('Deu PAR' if total % 2 == 0 else 'Deu Impar')
        if tipo == 'P':
            if total % 2 ==0:
                print('Você Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                break
        print('Vamos jogar')

Par_Impar()