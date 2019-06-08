n = int(input())
if n == 3:
    print(0)
else:
    barbante = n * (n - 3)
    for i in range(1, n - 1):
        barbante -= i
    print(barbante + 1)
