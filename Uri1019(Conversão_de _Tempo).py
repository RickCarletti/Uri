N = int(input())
h = N//60//60
m = N//60 - h*60
s = N - h * 60 * 60 - m * 60
print('{}:{}:{}'.format(h, m, s), end='\n')
