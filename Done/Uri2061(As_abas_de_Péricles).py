N, M = map(int, input().split())
for i in range(M):
    N -= 1 if input() == 'clicou' else -1
print(N)
