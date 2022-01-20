from datetime import date
def idade_alistamento():
    idade = int(input('Qual a sua idade? '))

    if idade < 18:
        falta = 18 - idade
        print('Você ainda não tem idade para se alistar!')
        print('Falta {} anos para você se alistar!'.format(falta))
    elif idade == 18:
        print('Você está na idade de se alistar!')
    elif idade > 18:
        falta = (18 - idade) * (-1)
        print('Você passou da idade de se alistar!')
        print('Passou {} anos para você se alistar!'.format(falta))

def ano_alistamento():
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não têm 18 anos. Ainda falta {} anos para o alistamento.'.format(saldo))
    elif idade > 18:
        saldo = idade -18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
ano_alistamento()
