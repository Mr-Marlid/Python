def F(S,s):
    if S!="":
        s = s + S[0]
        F(S[1:],s)
        F(S[1:],s.swapcase())
    else:
        global s1
        s1 = s1.replace(s,"*"*len(s))
        
s1 = input("Введите имя редактируемого файла: ")
s2 = input("Введите имя файла со служебными словами: ")
s3 = input("Введите имя итогового файла: ")
f = open(s2,'r')
s2 = f.read().split()
f.close()
f = open(s1,'r')

s1 = f.read()
 
for i in range(len(s2)):
    F(s2[i],"")
     
f.close()
print(s1)
f = open(s3,'w')
f.write(s1)
f.close()

