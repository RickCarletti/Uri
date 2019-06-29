p, j1, j2, r, a = map(int, input().split())
escolha1 = 'par' if p == 1 else 'impar'
result = j1 + j2
win = 'par' if result % 2 == 0 else 'impar'
if r == 0 and a == 0:
    pwin = 'Jogador 1 ganha!' if win == escolha1 else 'Jogador 2 ganha!'
else:
    pwin = 'Jogador 1 ganha!' if (r == 1 and a == 0) or (r == 0 and a == 1)else 'Jogador 2 ganha!'
print(pwin)
