
n=0
with open("2a.txt") as file:
    a = [row.strip() for row in file]

for i in range(int(a[0])+1):
    print(a[i])
    a[i] = int(a[i])
for i in range(1,a[0]-4):
    for j in range(i+4,a[0]+1):
        print(a[i],a[j])
        if (a[i]+a[j])%2==1 and (a[i]*a[j])%13==0:
            n+=1
f3 = open('2a.txt','w')
f3.write(str(n))
f3.close()
n=0
with open("2b.txt") as file:
    a2 = [row.strip() for row in file]
for i in range(int(a2[0])+1):
    a2[i] = int(a2[i])
for i in range(a2[0]-4):
    for j in range(i+4,a2[0]+1):
        if (a2[i]+a2[j])%2==1 and (a2[i]*a2[j])%13==0:
            n+=1
f4 = open('2b.txt','w')
f4.write(str(n))
f4.close()