lar = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
are = lar*alt
print('Sua parede tem a dimensão de {} m X {} m e sua área é de {} m.'.format(lar, alt, are))
tinta = are/2
print('Para pintar essa parede, você precisará de {:.0f} L de tinta.'.format(tinta))
