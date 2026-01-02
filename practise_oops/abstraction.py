from abc import ABC, abstractmethod
# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
# Child class
class Rectangle(Shape):

    def area(self):
        print("Area of rectangle = length * breadth")


r = Rectangle()
r.area()
