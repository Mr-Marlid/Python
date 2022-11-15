class Cat():
    name=""
    color=""
    weight=""
    def __init__ (self, newName, newColor, newWeight):
        self.name = newName
        self.color = newColor
        self.weight = newWeight
        print ("Создан кот")
    def meow(self):
        print("Cat named " + self.name + ", " + self.color + " color and weight " + self.weight + " kg say MEOW")



a = input()
b = input()
c = input()
myCat = Cat(a,b,c)
myCat.meow()