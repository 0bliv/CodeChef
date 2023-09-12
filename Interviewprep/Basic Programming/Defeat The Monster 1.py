t = int(input())
for i in range(t):
    H, X, Y = map(int, input().split())
    if Y >= X:
        print('0')
    else:
        print('1')