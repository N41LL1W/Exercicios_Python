from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print('O angulo {}, tem como: seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
