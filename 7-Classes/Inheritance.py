class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal("Mammal")
m.eat()
print(m.age)