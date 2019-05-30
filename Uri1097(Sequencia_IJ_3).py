i = 1
j = 3
while i < 10:
    j = j + 5
    x = 0
    while x < 3:
        x = x + 1
        j = j - 1
        print('I={} J={}'.format(i, j))
    i = i + 2
