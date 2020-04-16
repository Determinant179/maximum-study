import math

def desc(a, b, c):
    descrim = b * b - 4 * a * c
    x1 = (-b + math.sqrt(descrim))/(2 * a)
    x2 = (-b - math.sqrt(descrim))/(2 * a)

    return [x1, x2]


def main():
    a2 = float(input("Введите а: "))
    b2 = float(input("Введите b: "))
    c2 = float(input("Введите c: "))

    y = desc(a2, b2, c2)

    y1 = y[0]
    y2  = y[1]

    print("Корни: " + str(y1) + ", " + str(y2))

    return 0

main()