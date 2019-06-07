X = int(input())
Y = int(input())
if X < Y:
    inicio = X + 1
    fim = Y
else:
    inicio = Y + 1
    fim = X
while inicio < fim:
    if inicio % 5 == 2 or inicio % 5 == 3:
        print(inicio, end='\n')
    inicio = inicio + 1
