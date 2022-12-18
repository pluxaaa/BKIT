import math
import sys

def CoefInput(prompt):
    while True:
        print(prompt)
        try:
            coef = float(input())

        except ValueError:
            print("Ошибка ввода; введите число\n")

        else:
            print("Вы ввели: ", coef)
            break
    return coef

def GetRoots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D >= 0:
        D = math.sqrt(D)
        if D == 0:
            t = -b / (2 * a)
            if t >= 0:
                result.append(math.sqrt(t))
                result.append(-1 * math.sqrt(t))
                return result
            else:
                return result


        if D > 0:
            t1 = (-b + D) / (2 * a)
            t2 = (-b - D) / (2 * a)
            if t1 > 0:
                result.append(math.sqrt(t1))
                result.append(-1 * math.sqrt(t1))
            if t2 > 0:
                result.append(math.sqrt(t2))
                result.append(-1 * math.sqrt(t2))
            if (t1 < 0 and t2 < 0):
                return result

            return result
    else:
        return result


def main():
    while True:
        a = CoefInput('Введите коэффициент  A')
        if a != 0:
            break
        else:
            print("Коэффициент A не должен равняться 0\n")

    b = CoefInput('\nВведите коэффициент  B')
    c = CoefInput('\nВведите коэффициент  C')

    roots = GetRoots(a, b, c)

    if len(roots) != 0:
        print("\nОтвет: ")
        for i in range(len(roots)):
            print(i+1, "-й корень:", roots[i])
    else:
        print("\nНет действительных корней")


if __name__ == "__main__":
    main()
