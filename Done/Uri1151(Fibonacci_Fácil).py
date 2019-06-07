def fibonacci(cont):
    if cont == 1:
        fibonacci_lista = [0]
        return fibonacci_lista
    else:
        fibonacci_lista = [0, 1]
        for cont in range(2, cont):
            fibonacci_lista.append(fibonacci_lista[len(fibonacci_lista)-2]+fibonacci_lista[len(fibonacci_lista)-1])
        return fibonacci_lista


N = int(input())
fibonacci_lista = fibonacci(N)
print(' '.join(map(str, fibonacci_lista)), end='\n')
