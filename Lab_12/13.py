f = open('elements.txt','r')
a = [""] * 118
for i in range(118): 
    a[i] = [""] * 3 
for i in range(118):
    s = f.readline().split(',')
    s1 = s[2]
    s2 = s1[0:-1]
    a[i][0] += s[0]
    a[i][1] += s[1]
    a[i][2] += s2

f.close()
while s!="":
    s = input()
    try:
        
        x = int(s)
        
        if x>0 and x<119:
            x -=1
            print( a[x][1], a[x][2], a[x][0])
        else:
            print("Такого пока не нашли:(")
    except ValueError:
        for i in range (118):
            if a[i][1]==s or a[i][2]==s:
                print(a[i][0], a[i][1], a[i][2])
                break   
            
        print("Такого пока не нашли:(")