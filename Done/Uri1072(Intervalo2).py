fora = 0
dentro = 0
N = int(input())
while N > 0:
    X = int(input())
    if 10 <= X <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
    N = N - 1
print('{} in\n{} out'.format(dentro, fora), end='\n')
