class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


flying_fish = FlyingFish()
flying_fish.fly()
flying_fish.swim()
