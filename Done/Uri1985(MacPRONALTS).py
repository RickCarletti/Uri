preco = {1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}
soma = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    soma += preco[x] * y
print('{:.2f}'.format(soma))
