from cls_animal import Animal

class Bird(Animal):
    def __init__(self, name, color, wings, melody):
        super().__init__(name, color)
        self.wings = wings
        self.melody = melody

    def fly(self):
        print(f"{self.name} is flying with its {self.wings} {self.color} wings!")

    def sing(self):
        print((self.melody + " ") * 3)

class Owl(Bird):
    def __init__(self, name, color, wings, melody, degree):
        super().__init__(name, color, wings, melody)
        self.degree = degree

    def neck_twist(self):
        print(f"{self.name} is doing a {self.degree} degree neck twist.")

class Woodpecker(Bird):
    def __init__(self, name, color, wings, melody, strength):
        super().__init__(name, color, wings, melody)
        self.strength = strength

    def make_hole(self):
        print("kkkkkkdfdsgvxckvnfjdshfds " * self.strength)