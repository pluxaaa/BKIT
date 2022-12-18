import random
import sys
import math

def get_num(index, promt):
    try:
        num_str = sys.argv[index]
    except:
        print(promt)
        num_str = input()

    if not num_str.isalpha():
        num = float(num_str)
    else:
        print("Коэффициент задан некорректно. Он будет задан рандомно от 1 до 10")
        num = random.randint(1, 10)
        print(num)
    return num

def get_roots(a, b, c):
    result = []
    if a == 0:
        print("коэффициент А не может быть равне нулю. он будет задан рандомно от 1 до 10")
        a = random.randint(1, 10)
        print(a)
    D = b * b - 4 * a * c
    if D == 0.0:
        t = -b / (2.0 * a)
        x1 = - math.sqrt(t)
        x2 = math.sqrt(t)
        result.append(x1)
        if x1 != 0:
            result.append(x2)
    elif D > 0.0:
        t1 = (- b + math.sqrt(D)) / (2.0 * a)
        if t1 > 0.0:
            x1_1 = math.sqrt(t1)
            x1_2 = - math.sqrt(t1)
            result.append(x1_1)
            result.append(x1_2)

        t2 = (- b - math.sqrt(D)) / (2.0 * a)
        if t2 > 0.0:
            x2_1 = math.sqrt(t2)
            x2_2 = - math.sqrt(t2)
            result.append(x2_1)
            result.append(x2_2)

    return result

def main():
    a = get_num(1, "Введите коэффициент А:")
    b = get_num(2, "Введите коэффициент В:")
    c = get_num(3, "Введите коэффициент C:")

    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print("Один корень: {}".format(roots[0]))
    elif len_roots == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))
    elif len_roots == 4:
        print("Четыре корня: {}; {}; {}; {};".format(roots[0], roots[1], roots[2], roots[3]))

    # если сценарий запущен из командной строки
if __name__ == "__main__":
    main()