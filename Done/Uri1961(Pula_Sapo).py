P, N = map(int, input().split())
alturas = list(map(int, input().split()))
for i in range(N-1):
    if abs(alturas[i+1] - alturas[i]) > P:
        win = False
        break
    else:
        win = True
if win:
    print('YOU WIN')
else:
    print('GAME OVER')
