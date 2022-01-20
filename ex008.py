med=float(input('Qual a medida? '))
km=med*0.001
hm=med*0.01
dam=med*0.1
dm=med*10
cm=med*100
mm=med*1000
print('Os {} metros, equivalem a {} Km!'.format(med, km))
print('Os {} metros, equivalem a {} Hm!'.format(med, hm))
print('Os {} metros, equivalem a {:.1f} Dam!'.format(med, dam))
print('Os {} metros, equivalem a {:.0f} Dm!'.format(med, dm))
print('Os {} metros, equivalem a {:.0f} Cm!'.format(med, cm))
print('Os {} metros, equivalem a {:.0f} Mm!'.format(med, mm))
