tr = list(map(float, input().split()))
A = tr[0]
B = tr[1]
C = tr[2]
pi = 3.14159
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'
      .format((A * C)/2, pi * C**2, ((A + B) * C)/2, B*B, A*B), end='\n')
