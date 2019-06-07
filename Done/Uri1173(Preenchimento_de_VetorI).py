V = list(map(int, input().split()))
N = V
for i in range(10):
    print('N[{}] = {}'.format(i, N[i]))
    N.append(N[i] * 2)
