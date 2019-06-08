QT = int(input())
for i in range(QT):
    text = list(map(str, input().split()))
    N, M = map(int, input().split())
    soma = N + M
    if soma % 2 == 0:
        win = 'PAR'
    else:
        win = 'IMPAR'
    for j in range(len(text)):
        if text[j] == win:
            print(text[j-1])
            break
