A = dict()
s = input().split()
for i in range(len(s)):
    if A.get(s[i])!=None:
        print(A[s[i]], end=' ')
        A[s[i]] += 1
    else:
        print("0", end=' ')
        A[s[i]] = 1
        
