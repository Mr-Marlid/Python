f = open('11_10.txt','r')

A = dict()
s = f.readline().split()
a = list()
b = list()
a.append(s[0])
b.append(s[1])

while s:
    key = s[0],s[1]
    value = s[2]
    if A.get(key)!=None:
        value = str( int(value) + int(A.get(key)) )
    else:
        if a.count(s[0])==0:
            a.append(s[0])
        if b.count(s[1])==0:
            b.append(s[1])        
    A[key] = value
    
    s = f.readline().split()
f.close()
print(a)
print(b)
for i in range(len(a)):
    print(a[i]+":")
    for j in range (len(b)):
        try:
            print(b[j], A[a[i],b[j]])
        except KeyError:
            s=""
    

