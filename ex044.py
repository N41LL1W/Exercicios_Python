def Pagamento():
    valor = float(input('Preço das compras: R$'))
    print('''Escolha a forma de pagamento:
    [1] - À vista no dinheiro ou cheque.
    [2] - À vista no cartão.
    [3] - Em 2x no cartão.
    [4] - 3x ou mais no cartão.''')
    pgto = int(input('Tipo de pagamento: '))

    if pgto == 1:
        forma = ('à vista dinheiro ou cheque')
        desc = ('10%')
        saldo = valor - (valor * 0.1)
        print('''Suas compras ficaram R${},
        a forma de pagamento escolhida foi {},
        com um desconto de {},
        então seu pagamento será de R${}.'''.format(valor, forma, desc, saldo))
    elif pgto == 2:
        forma = ('à vista cartão')
        desc = ('5%')
        saldo = valor - (valor * 0.05)
        print('''Suas compras ficaram R${},
        a forma de pagamento escolhida foi {},
        com um desconto de {},
        então seu pagamento será de R${}.'''.format(valor, forma, desc, saldo))
    elif pgto == 3:
        forma = ('2x no cartão')
        saldo = valor
        print('''Suas compras ficaram R${},
        a forma de pagamento escolhida foi {},
        então seu pagamento será de R${}.'''.format(valor, forma, saldo))
    elif pgto == 4:
        forma = ('3x ou mais no cartão')
        desc = ('20%')
        saldo = valor + (valor * 0.2)
        print('''Suas compras ficaram R${},
        a forma de pagamento escolhida foi {},
        com juros de {},
        então seu pagamento será de R${}.'''.format(valor, forma, desc, saldo))
    else:
        print('Forma invalida!')
        Pagamento()

Pagamento()