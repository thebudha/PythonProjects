class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, object))  # True
print(issubclass(Mammal, object))  # True