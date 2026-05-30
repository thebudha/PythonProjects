class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)  # True
print(m.weight)  # True