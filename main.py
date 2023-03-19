import math

"""Проценты"""


def perc_of_num(number, percent):
    """Нахождение процента от числа"""

    result = number/100* percent
    print(f'{percent}% от {number} это {result}')
    return result


def perc_change(number_1, number_2):
    """Нахождение процентного изменения"""

    result = ((number_2 - number_1)/number_1) * 100

    if number_1 > number_2:
        print(f'Число увеличилось на {result}%')
    elif number_1 < number_2:
        print(f'Число уменьшилось на {result}%')
    return result


def relation(number_1, number_2):
    """Сколько процентов, сотавляет число №1 от числа №2"""

    result = number_1 / number_2 * 100
    print(f'Столько {result}%, составляет {number_1} от {number_2}')

    return result


"""Фигуры"""


def sq_of_tringle_high(base, height):
    """Нахождение площади треугольника через основание высоту"""

    result = 0.5 * base * height
    print(f'Тругольник имеет площадь {result}, имея высоту {height} и основание {base}')
    return result


def sq_of_tringle_geron(a,b,c):
    """Нахождение площади треугольника через формулу герона"""

    p = 0.5 * (a + b + c)

    result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'Треугольник имеет площадь {result} со сторонами {a}, {b}, {c}')
    return result


def sq_of_circle(radius):
    """Нахождение площади круга имея радиус"""

    pi = 9.869604401**0.5
    result = pi * radius ** 2
    print(f'Круг с радиусом {radius} имеет площадь {result} ')
    return result


def right_polyhedron(num_of_sides, len_of_sides):
    """Нахождение площади правильного многогранника по количеству его сторон и их длине"""

    result = (num_of_sides * len_of_sides ** 2)/(4 * math.tan(6.2832/(2*num_of_sides)))
    print(f'Многогранник с {num_of_sides} сторонами, с длинной {len_of_sides} имеет площадь {result}')
    return result


def teor_of_pifagor(side_1, side_2,hypotenuse):
    """Нахождение стороны треугольника по пифагору"""

    if side_1 == 0 or side_2 == 0:
        result = (hypotenuse**2 - (max(side_1, side_2))**2) ** 0.5
        print(f'Треугольник со сторонами {max(side_1,side_2)}, {result} и гипотензой {hypotenuse}')
    elif hypotenuse == 0:
        result = ((side_1**2 + side_2**2) ** 0.5)
        print(f'Треугольник со сторонами {max(side_1, side_2)}, {min(side_1, side_2)} и гипотензой {result}')
    else:
        print('Если вы хотите найти сторону, то введите ее значение равное 0')


"""Числа"""


def round_up(number, num_after_com):
    """Округление числа до какого-то числа после запятой"""

    x = int(number * 10**(num_after_com+1))
    print(number)
    print(x)
    if x % 10 > 4:
        x = x // 10 + 1
        result = x / 10 ** num_after_com
    else:
        x = x // 10
        result = x / 10 ** num_after_com

    print(f'Если округлить {number} до {num_after_com} цифр после запятой, то получится {result}')
    return result


def factorial(number):
    """Нахождение факториала числа"""

    result = 1
    for i in range(number,1,-1):
        result = result * i

    print(f'Факториал {number}! равен {result}')
    return result


def arithmetic_and_geometric(list_of_num):
    """Нахождение среднего арифметического и геометрического"""

    if type(list_of_num) != list:
        print('Введите список чисел')
        return 0
    arith_res = 0
    geo_res = 1
    for i in list_of_num:
        arith_res += i
        geo_res *= i

    arith_res /= len(list_of_num)
    geo_res = geo_res ** (1/len(list_of_num))
    print(f'Среднее арифметическое {arith_res}, среднее геометрическое {geo_res} из списка {list_of_num}')
    return arith_res, geo_res


