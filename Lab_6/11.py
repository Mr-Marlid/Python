x = int(input())
y = x + 1
n=0
while x!=0:
    if x>y:
        n+=1
    y = x
    x = int(input())
print(n)
    