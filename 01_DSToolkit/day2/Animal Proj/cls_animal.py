class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"Name: {self.name}, Color: {self.color}")