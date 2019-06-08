N = int(input())
M = N//1000
D = (N - 1000 * M)//500
C = (N - 1000 * M - 500 * D)//100
L = (N - 1000 * M - 500 * D - 100 * C)//50
X = (N - 1000 * M - 500 * D - 100 * C - 50 * L)//10
V = (N - 1000 * M - 500 * D - 100 * C - 50 * L - 10 * X)//5
I = (N - 1000 * M - 500 * D - 100 * C - 50 * L - 10 * X - 5 * V)//1
lista = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
if M != 0:
    print(lista[0]*M, end='')
if C + D * 5 == 9:
    print(lista[1], end='')
else:
    if D != 0:
        print(lista[2], end='')
    if C == 4:
        print(lista[3], end='')
    elif C != 0:
        print(lista[4]*C, end='')
if X + L * 5 == 9:
    print(lista[5], end='')
else:
    if L != 0:
        print(lista[6], end='')
    if X == 4:
        print(lista[7], end='')
    elif X != 0:
        print(lista[8]*X, end='')
if I + V * 5 == 9:
    print(lista[9], end='')
else:
    if V != 0:
        print(lista[10], end='')
    if I == 4:
        print(lista[11], end='')
    elif I != 0:
        print(lista[12]*I, end='')
print()
