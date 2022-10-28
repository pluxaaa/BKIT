from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from math import pi

class Circle(Figure):

    fType = "круг"
    @classmethod
    def getType(cls):
        return cls.fType

    def __init__(self, rad, col):
        self.r = rad
        self.fc = FigureColor()
        self.fc.colorproperty = col

    def square(self):
        return pi * pow(self.r, 2)

    def __repr__(self):
        return '{} {} радиусом {} и площадью {:.3f}.'.format(
            self.fc.colorproperty,
            self.getType(),
            self.r,
            self.square()
        )


#cir = Circle(3, "Красный")
#print(cir)