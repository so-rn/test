from cls_bird import Owl, Woodpecker
from cls_fish import Salmon, Shark

owl = Owl("Hooty", "Brown", 2, "wio wio again miooo", 270)
woodpecker = Woodpecker("Woody", "Red", 2, "dsfdsffsfd", 5)
salmon = Salmon("Sammy", "Pink", 20)
shark = Shark("Bruce", "White", 45)

print(" Owl ")
owl.introduce()
owl.fly()
owl.sing()
owl.neck_twist()

print("\n  Woodpecker ")
woodpecker.introduce()
woodpecker.make_hole()

print("\n Salmon ")
salmon.introduce()
salmon.swim()

print("\n Shark ")
shark.introduce()
shark.bite()