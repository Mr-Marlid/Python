a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
k = int(input())
a = a[:k] + a[k+1:]
print(a)