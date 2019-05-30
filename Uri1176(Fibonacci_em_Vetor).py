def Fibonacci_List(X):
    Fibonacci_List = [0, 1]
    for X in range(2, X+1):
        Fibonacci_List.append(Fibonacci_List[len(Fibonacci_List) - 2] + Fibonacci_List[len(Fibonacci_List) - 1])
    return Fibonacci_List


T = int(input())
Nold = -1
for T in range(T):
    N = int(input())
    if N > Nold:
        Nold = N
        Lista_Fibonacci = Fibonacci_List(N)
    print('Fib({}) = {}'.format(N, Lista_Fibonacci[N]))
