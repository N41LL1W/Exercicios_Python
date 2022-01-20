def Pessoa():

    soma = 0
    media = 0
    velho = 0
    nomevelho = ''
    menos = 0
    sanos = ''
    sm = ''

    for p in range(1, 5):
        print('----- {}ª PESSOA -----'.format(p))
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip()
        soma += idade

        if p == 1 and sexo in 'Mm':
            velho = idade
            nomevelho = nome
        if sexo in 'Mn' and idade > velho:
            velho = idade
            nomevelho = nome

        if sexo in 'fF' and idade < 20:
            menos += 1

    if velho == 1:
        sanos = ''
    else:
        sanos = 's'

    if menos == 1:
        sm = ''
    else:
        sm = 'es'

    media = soma / p
    if velho != 0:
        print('O homem mais velho tem {} ano{} e se chama {}.'.format(velho, sanos, nomevelho.capitalize()))
    else:
        print('Não temos homens nesse grupo.')

    print('A média de idade desse grupo é {:.0f} anos'.format(media))
    print('E nesse grupos temos {} mulher{} com menos de 20 anos'.format(menos, sm))
Pessoa()