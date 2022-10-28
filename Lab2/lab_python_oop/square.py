from lab_python_oop.figure import Figure
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import FigureColor

class Square(Rectangle):

    fType = "квадрат"
    @classmethod
    def getType(cls):
        return cls.fType

    def __init__(self, sd, col):
        self.side = sd
        super().__init__(self.side, self.side, col)

    def square(self):
        return pow(self.side, 2)

    def __repr__(self):
        return '{} {} со стороной {} и площадью {}.'.format(
            self.fc.colorproperty,
            self.getType(),
            self.side,
            self.square()
        )