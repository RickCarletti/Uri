val = list(map(float, input().split()))
A = val[0]
B = val[1]
C = val[2]
if abs(B - A) < C < A + B and abs(C - A) < B < C + A and abs(B - C) < A < B + C:
    peri = A + B + C
    print('Perimetro = {:.1f}'.format(peri), end='\n')
else:
    area = (A + B) * C / 2
    print('Area = {:.1f}'.format(area), end='\n')
