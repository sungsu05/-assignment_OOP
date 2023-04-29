from abc import abstractmethod
from math import pi
class Shape:

    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return int((self.radius ** 2) * pi)


class Rectangle(Shape):
    def __init__(self,length,widht):
        self.length = length
        self.widht = widht

    def get_area(self):
        return self.length * self.widht

circle = Circle(10)
print(circle.get_area())

rectangle = Rectangle(3, 7)
print(rectangle.get_area())