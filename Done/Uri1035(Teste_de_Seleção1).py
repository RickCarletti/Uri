n = list(map(int, input().split()))
A = n[0]
B = n[1]
C = n[2]
D = n[3]
if B > C and D > A and C + D > A + B and C >= 0 and D >= 0 and A % 2 == 0:
    print('Valores aceitos', end='\n')
else:
    print('Valores nao aceitos', end='\n')
