class Point():
    x = 0
    y = 0

    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY

    def get (self):
        print("x: " + self.x + " y: "+ self.y)

    def set (self, newX, newY):
        self.x = newX
        self.y = newY

myPoint = Point(int(input()), int(input()))
myPoint.get()
myStringVar.set(int(input()), int(input()))
myPoint.get()
