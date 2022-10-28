from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import cowsay

def main():
    r = Rectangle(3, 6, "Синий")
    c = Circle(5, "Зеленый")
    s = Square(3, "Красный")

    cowsay.cat(str(r) + '\n' + str(c) + '\n' + str(s))

if __name__ == "__main__":
    main()