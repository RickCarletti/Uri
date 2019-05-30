N = int(input())
X = list(map(int, input().split()))
menor = X[0]
for N in range(N-1):
    if X[N+1] < menor:
        menor = X[N+1]
print('Menor valor: {}\nPosicao: {}'.format(menor, X.index(menor)))
