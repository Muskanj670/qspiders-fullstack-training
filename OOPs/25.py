# Abstraction

from abc import ABC, abstractmethod, abstractstaticmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod   
    def perimeter(self):
        pass

    @abstractstaticmethod
    def get_height():
        pass

    @abstractstaticmethod
    def get_width():
        pass


class Rectangle(Shape):

    def __init__(self):
        self.height = self.get_height()
        self.width = self.get_width()

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (2*(self.height + self.width))

    @staticmethod
    def get_height():
        h = int(input("Enter the height of the rectangle: "))
        return h

    @staticmethod
    def get_width():
        w = int(input("Enter the width of the rectangle: "))
        return w


class Square(Shape):
    def __init__(self):
        self.side = self.get_height()

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    @staticmethod
    def get_height():
        s = int(input("Enter the side of the square: "))
        return s

    @staticmethod
    def get_width():
        pass

obj = Rectangle()
print(f'Area of the rectangle is: {obj.area()}.')
print(f'Perimeter of the rectangle is: {obj.perimeter()}.')

obj2 = Square()
print(f'Area of the square is: {obj.area()}.')
print(f'Perimeter of the square is: {obj.perimeter()}.')