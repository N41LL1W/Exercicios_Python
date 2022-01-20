from math import hypot
caop = float(input('Comprimento do cateto oposto: '))
caad = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(caop, caad)))
