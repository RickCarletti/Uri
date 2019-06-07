X = list(map(int, input().split()))
cont = -1
N = 1
while cont <= 0:
    cont = X[N]
    N = N + 1
soma = 0
X = X[0]
while cont > 0:
    soma = soma + X
    X = X + 1
    cont = cont - 1
print(soma, end='\n')
