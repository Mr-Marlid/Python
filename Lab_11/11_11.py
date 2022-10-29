def F(x,s):
    if A.get(x)!=None:
        return F(A.get(x),s+1)
    else:
        return s
    
    
n = int(input())
l = list()
A = dict()
for i in range(n-1):
    a,b = input().split()
    if l.count(a)==0:
        l.append(a)  
    if l.count(b)==0:
        l.append(b)  
    A[a] = b
print()
for i in range(n):
    print(l[i], F(l[i],0))
    