from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):

    fType = "прямоугольник"
    @classmethod
    def getType(cls):
        return cls.fType

    def __init__(self, length, width, col):
        self.l = length
        self.w = width
        self.fc = FigureColor()
        self.fc.colorproperty = col

    def square(self):
        return self.l * self.w

    def __repr__(self):
        return '{} {} со сторонами {} и {}, площадью {}.'.format(
            self.fc.colorproperty,
            self.getType(),
            self.w,
            self.l,
            self.square()
        )