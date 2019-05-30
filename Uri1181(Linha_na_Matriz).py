L = int(input())
T = str(input())
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
for i in range(12):
    soma += matriz[L][i]
if T == 'S':
    print('{:.1f}'.format(soma), end='\n')
elif T == 'M':
    print('{:.1f}'.format(soma/12), end='\n')
