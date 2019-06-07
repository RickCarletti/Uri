def Fatorial(n):
    fatorial = 1
    for n in range(1, n+1):
        fatorial = fatorial * n
    return fatorial

N = int(input())
print(Fatorial(N), end='\n')
