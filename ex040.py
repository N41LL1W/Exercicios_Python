def media():
    n1 = float(input('Digite a nota do 1º bimestre: '))
    n2 = float(input('Digite a nota do 2º bimestre: '))
    n3 = float(input('Digite a nota do 3º bimestre: '))
    n4 = float(input('Digite a nota do 4º bimestre: '))

    media = (n1 + n2 + n3 + n4) / 4

    if media < 5:
        print('Sua média foi {} você está de RECUPERAÇÃO!!!'.format(media))
    elif media >= 5:
        print('Sua média foi {}, você está APROVADO!!!'.format(media))
    elif media == 10.0:
        print('Você tirou a nota MAXIMA, meus parabens, está APROVADO!!!')

media()
