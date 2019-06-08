X = float(input())
if X > 0:
    print('+{:.4e}'.format(X).upper())
elif str(X)[0] == '-':
    print('{:.4e}'.format(X).upper())
elif str(X)[0] == '+' or '0':
    print('+{:.4e}'.format(X).upper())
else:
    print('{:.4e}'.format(X).upper())
