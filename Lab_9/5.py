n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if ((i+j+1) == n ):
            a[i][j] = 1        
        elif i+j+1>n:
            a[i][j] = 2
        else :
            a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))