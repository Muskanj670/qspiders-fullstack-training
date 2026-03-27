# Hierarchical Inheritance

class Animal:
    @staticmethod
    def walk():
        print("Animal can Walk")

class Dog(Animal):
    pass

class cat(Animal):
    pass
class Human(Animal):
    pass

obj1 = Dog()
obj2 = cat()
obj3 = Human()

obj1.walk()
obj2.walk()
obj3.walk()