N = int(input())
L = list(map(int, input().split()))
m2, m3, m4, m5 = 0, 0, 0, 0
for i in L:
    m2 += 1 if i % 2 == 0 else 0
    m3 += 1 if i % 3 == 0 else 0
    m4 += 1 if i % 4 == 0 else 0
    m5 += 1 if i % 5 == 0 else 0
print('{} Multiplo(s) de 2\n{} Multiplo(s) de 3\n{} Multiplo(s) de 4\n{} Multiplo(s) de 5'.format(m2, m3, m4, m5))
