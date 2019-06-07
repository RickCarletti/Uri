N = []
X = int(input())
for i in range(1000):
    N.append(i % X)
    print('N[{}] = {}'.format(i, N[i]))
