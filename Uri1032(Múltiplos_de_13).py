X = int(input())
Y = int(input())
soma = 0
if X < Y:
    inicio = X
    fim = Y
else:
    inicio = Y
    fim = X
while inicio <= fim:
    if not inicio % 13 == 0:
        soma = soma + inicio
    inicio = inicio + 1
print(soma, end='\n')
