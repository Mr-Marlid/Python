#Задание 3 Разработать класс «Многочлен» от одной переменной.
#Многочлен задаётся степенью и массивом коэффициентов. Предусмотреть
#методы вычисления значения многочлена для заданного аргумента, операции
#сложения, вычитания и умножения многочленов.
class Mnogochlen():
    def __init__(self,NewStepen,NewMassiv):
        self.stepen = NewStepen
        self.massiv = NewMassiv
    
    def argument(self, argument):
        m = self.massiv
        x = self.stepen
        sum = 0
        for i in range(x):
            sum += pow(argument,i) * m[i]
        return sum
        
           
            

def create():
    print("Введите самую высокую степень: ")
    while True:
        try:
            n = int(input())
            break
        except:
            print("Введите ЧИСЛО!")
    n += 1
    x = [0]*(n)
    for i in range(n):
        print("Введите коэффициент для x в степени " + str(i) +": ")
        while True:
            try:
                x[i] = int(input())
                break
            except:
                print("Ты не понял, тут Я устанавливаю правила, ВВЕДИ ЧИСЛО!")    
    
    return n,x

def sum():
    n,x = create()
    MyMn1 = Mnogochlen(n,x)
    n,x = create()
    MyMn2 = Mnogochlen(n,x)
    m1 = MyMn1.massiv
    x1 = MyMn1.stepen
    m2 = MyMn2.massiv
    x2 = MyMn2.stepen    
    s = ""
    if (x1>x2):
        for i in range(x1):
            try:
                if m2[i] + m1[i] != 0:
                    if i==0:
                        s += str(m2[i] + m1[i]) + " "
                    else:
                        s += str(m2[i] + m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m1[i]) + "x^" + str(i) + " "
    else:
        for i in range(x2):
            try:
                if m2[i] + m1[i] != 0:
                    if i==0:
                        s += str(m2[i] + m1[i]) + " "
                    else:
                        s += str(m2[i] + m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m2[i]) + "x^" + str(i) + " "
    return s   


def arg():
    n,x = create()
    MyMn1 = Mnogochlen(n,x)
    print("Введите аргумент")
    while True:
        try:
            a = int(input())
            break
        except:
            print("О боже...")
    return MyMn1.argument(a)
    
    
def vich():
    n,x = create()
    MyMn1 = Mnogochlen(n,x)
    n,x = create()
    MyMn2 = Mnogochlen(n,x)
    m1 = MyMn1.massiv
    x1 = MyMn1.stepen
    m2 = MyMn2.massiv
    x2 = MyMn2.stepen    
    s = ""
    if (x1>x2):
        for i in range(x1):
            try:
                if m2[i] - m1[i] != 0:
                    if i==0:
                        s += str(m2[i] - m1[i]) + " "
                    else:
                        s += str(m2[i] - m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m1[i]) + "x^" + str(i) + " "
    else:
        for i in range(x2):
            try:
                if m2[i] - m1[i] != 0:
                    if i==0:
                        s += str(m2[i] - m1[i]) + " "
                    else:
                        s += str(m2[i] - m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m2[i]) + "x^" + str(i) + " "
    return s   


def pr():
    n,x = create()
    MyMn1 = Mnogochlen(n,x)
    n,x = create()
    MyMn2 = Mnogochlen(n,x)
    m1 = MyMn1.massiv
    x1 = MyMn1.stepen
    m2 = MyMn2.massiv
    x2 = MyMn2.stepen    
    s = ""
    if (x1>x2):
        for i in range(x1):
            try:
                if m2[i] * m1[i] != 0:
                    if i==0:
                        s += str(m2[i] * m1[i]) + " "
                    else:
                        s += str(m2[i] * m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m1[i]) + "x^" + str(i) + " "
    else:
        for i in range(x2):
            try:
                if m2[i] * m1[i] != 0:
                    if i==0:
                        s += str(m2[i] * m1[i]) + " "
                    else:
                        s += str(m2[i] * m1[i]) + "x^" + str(i) + " "
            except:
                s += str(m2[i]) + "x^" + str(i) + " " 
    return s




print("Команды: Сложение, Вычитание, Умножение, Задать аргумент")
print("Что вы хотите?")
g = input()
if g == "Сложение":
    print(sum())
elif g == "Вычитание":
    print(vich())
elif g == "Задать аргумент":
    print(arg())
elif g == "Умножение":
    print(pr())

    