import datetime
from datetime import date

def Categoria():
    atual = date.today().year
    ano = int(input('Ano de Nascimento: '))
    saldo = atual - ano
    print('Sua categoria é:')

    if saldo <= 9:
        print('MIRIM')
    elif saldo > 9 and saldo <= 14:
        print('INFANTIL')
    elif saldo > 14 and saldo <= 19:
        print('JÚNIOR')
    elif saldo > 18 and saldo <= 25:
        print('SÊNIOR')
    else:
        print('MASTER')

Categoria()
