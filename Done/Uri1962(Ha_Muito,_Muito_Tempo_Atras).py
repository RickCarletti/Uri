N = int(input())
ano = 2015
for i in range(N):
    T = int(input())
    anonovo = ano - T
    if anonovo > 0:
        print(anonovo, 'D.C.')
    else:
        print(abs(anonovo - 1), 'A.C.')
