N = str(input().strip())
if 'e' in N:
    N = str(N[:N.index('e')])
print(N[::-1])
