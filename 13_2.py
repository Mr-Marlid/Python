class Animal():
    name = ""

    def __init__ (self, newName):
        self.name = newName
        print("Родилось животное" + self.name)

    def eat (self):
        print ("Намнём")

    def getName (self):
        print(self.name)

    def setName (self, newName):
        self.name = newName

    def makeNoise (self):
        print(self.name + "говорит Гррр")


myAnimal = Animal(input())
myAnimal.eat()
myAnimal.getName()
myAnimal.setName(input())
myAnimal.getName()
myAnimal.makeNoise()
