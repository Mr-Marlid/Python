n = int(input())
s = 0
s1 = 0
for i in range (n-1):
    s1 += i + 1
    s += int(input())
s1 += n
print(s1-s)