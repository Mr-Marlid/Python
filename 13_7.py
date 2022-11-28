class Animal:

    __name: str

    def __init__(self, name):
        self.__name = name
        print(f"An animal called {name} was born!")

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, name): self.__name = name

    def eat(self, foodName):
        print(f'{self.__name} is eating {foodName}...')

    def makeNoise(self):
        print(f'{self.__name}\'s saying grrrrhh...')



class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight

    def makeNoise(self):
        print('Meow!')

class Dog(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight
        print('A dog\'s just arrived')

    def makeNoise(self):
        print(f'{super().name}\'s saying woof...')


if __name__ == "__main__":
    cat = Cat('Tom', 'Gray', 4)
    cat.makeNoise()

    animal = Animal('L')
    print('Animal\'s name is', animal.name)
    animal.name = 'Lololoshka'
    animal.eat('Humor')
    animal.makeNoise()

    dog1 = Dog('Pes', 'pink', 1.5)
    dog1.name = 'Gleb'
    print(dog1.name)
    dog1.makeNoise()
    dog1.eat('murders')
    dog2 = Dog('cat', 'violet', 3)
    dog2.name = 'Lom'
    print(dog2.name)
    dog2.makeNoise()
    dog2.eat('p**p')

