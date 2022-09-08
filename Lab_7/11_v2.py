a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
k = int(input())
for i in range(len(a)):
    if i > k :
        a[i-1] = a[i]
a = a[:-2]
print(a)