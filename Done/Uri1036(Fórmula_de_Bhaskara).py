n = list(map(float, input().split()))
A = n[0]
B = n[1]
C = n[2]
delta = B**2 - 4 * A * C
if delta >= 0 and A != 0:
    R1 = (0 - B + (delta)**(1/2)) / (2 * A)
    R2 = (0 - B - (delta)**(1/2)) / (2 * A)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(R1, R2), end='\n')
else:
    print('Impossivel calcular', end='\n')
