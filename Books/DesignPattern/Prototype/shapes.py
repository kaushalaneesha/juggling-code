import copy
class Shape:
    def clone(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        super().__init__()
        self.__height = height
        self.__width = width 

    def clone(self):
        return Rectangle(self.__height, self.__width)

rec = Rectangle(10, 15)
rec2 = rec.clone()
print(rec)
print(rec2)
print(rec is rec2)

    