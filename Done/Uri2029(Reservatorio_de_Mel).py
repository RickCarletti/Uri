while True:
    try:
        V = float(input())
        D = float(input())
        n = 3.14
        R = D / 2
        area = n * R**2
        h = V / area
        print('ALTURA = {:.2f}\nAREA = {:.2f}'.format(h, area))
    except EOFError:
        break
