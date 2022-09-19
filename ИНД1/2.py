n=0
with open("2a.txt") as file:
    a = [row.strip() for row in file]

for i in range(int(a[0])+1):
    a[i] = int(a[i])
for i in range(1,a[0]-4):
    for j in range(i+4,a[0]+1):
        if (a[i]+a[j])%2==1 and (a[i]*a[j])%13==0:
            n+=1
print("A ",n)






n=0
k=0
h=0
hn=0
kn=0
with open("2b.txt") as file:
    a2 = [row.strip() for row in file]
for i in range(int(a2[0])+1):
    a2[i] = int(a2[i])
    if i>0:
        if a2[i]%13==0:
            if a2[i]%2==1:
                kn+=1
            else:
                k+=1
        if a2[i]%2==1:
            hn+=1  
        else:
            h+=1
print (h,hn,k,kn)
for i in range(1,a2[0]-3):
    
    if a2[i]%13==0:
        if a2[i]%2==0:
            k-=1
            h1 = hn
            if a2[i+1]%2==1:
                h1-=1
            if a2[i+2]%2==1:
                h1-=1
            if a2[i+3]%2==1:
                h1-=1
            if a2[i+4]%2==1:
                h1-=1
            n+=h1
        else:
            kn-=1
            h1 = h
            if a2[i+1]%2==0:
                h1-=1
            if a2[i+2]%2==0:
                h1-=1
            if a2[i+3]%2==0:
                h1-=1
            if a2[i+4]%2==0:
                h1-=1
            n+=h1            
    else:
        if a2[i]%2==0:
            h-=1
            h1 = kn
            if a2[i+1]%2==1 and a2[i+1]%13==0:
                h1-=1
            if a2[i+2]%2==1 and a2[i+2]%13==0:
                h1-=1
            if a2[i+3]%2==1 and a2[i+3]%13==0:
                h1-=1
            if a2[i+4]%2==1 and a2[i+4]%13==0:
                h1-=1
            n+=h1
        else:
            hn-=1
            h1 = k
            if a2[i+1]%2==0 and a2[i+1]%13==0:
                h1-=1
            if a2[i+2]%2==0 and a2[i+2]%13==0:
                h1-=1
            if a2[i+3]%2==0 and a2[i+3]%13==0:
                h1-=1
            if a2[i+4]%2==0 and a2[i+4]%13==0:
                h1-=1
            n+=h1   
        print(i,h,hn,k,kn,n)
print("B ",n)
