class FigureColor:
    #цвет фигуры

    def __init__(self):
        self._color = None

    @property
    #getter
    def colorproperty(self):
        return self._color

    @colorproperty.setter
    #setter
    def colorproperty(self, value):
        self._color = value

    """
    def getColor(self):
        print(self._FigureColor)
        return self._FigureColor

    def setColor(self, value):
        self._FigureColor = value
    """

"""
color1 = FigureColor()
color1.colorproperty = "red"
print(color1._color)

color1._color = "blue"
print(color1._color)
"""
