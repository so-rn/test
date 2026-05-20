from cls_animal import Animal

class Fish(Animal):
    def __init__(self, name, color, speed):
        super().__init__(name, color)
        self.speed = speed

    def swim(self):
        print(f"{self.name}, the {self.color} fish, is swimming at {self.speed} km/h!", end=" ")

class Salmon(Fish):
    def swim(self):
        super().swim()
        print(" again ")

class Shark(Fish):
    def bite(self):
        print("fdgdfgfdgdfg dsfdsffdf fsdfdsfdsff")