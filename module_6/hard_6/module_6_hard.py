from math import pi, sqrt


class Figure(object):
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__color = [0, 0, 0]  # (список цветов в формате RGB)
        self.__sides = list()  # (список сторон(целые числа))
        # self.filled = filled  # Атрибуты(публичные): filled(закрашенный, bool)  ??????????

        self.set_color(*color)

        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            """
            Если кол-во сторон не ровно sides_count,
            то создать массив со сторонами, равными единице и в том кол-ве, которое требует фигура.
            """
            self.__sides = [1] * self.sides_count

    def get_color(self):
        """
        Метод get_color, возвращает список RGB цветов.
        """
        return self.__color

    def __is_valid_color(self, r, g, b):
        """
        Метод __is_valid_color - служебный, принимает параметры r, g, b,
        проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        """
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if (r in range(0, 256)
                    and g in range(0, 256)
                    and b in range(0, 256)):
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        """
        Метод set_color принимает параметры r, g, b - целые числа
        и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = list((r, g, b))

    def __is_valid_sides(self, sides):
        """
        Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        возвращает:
            True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        False - во всех остальных случаях.
        """
        if len(sides) == self.sides_count:
            for every_side in list(sides):
                if isinstance(every_side, int):
                    if every_side <= 0:
                        return False  # Если хоть одно из чисел меньше или равно нолю.
                else:
                    return False  # Если хоть один из элементов списка не является типом int
            """
            Здесь все проверки пройдены, вернём True
            """
            return True
        else:
            return False  # Кол-во новых сторон не равно кол-ву сторон объекта.

    def get_sides(self):
        """
        Метод get_sides должен возвращать значение атрибута __sides.
        """
        return self.__sides

    def __len__(self):
        """
        Метод __len__ должен возвращать периметр фигуры.
        """
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """
        Метод set_sides(self, *new_sides) должен принимать новые стороны,
            если их количество не равно sides_count, то не изменять,
            в противном случае - менять.
        """
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *length_circumference):
        """
        Все атрибуты и методы класса Figure
        Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
        """
        Figure.__init__(self, color, *length_circumference, filled=False)
        self.__radius = self._Figure__sides[0] / (2 * pi)

    def set_sides(self, *new_sides):
        """Переопределяет set_sides для изменения атрибута __radius
        """
        if len(new_sides) == 1:
            if isinstance(*new_sides, int):
                if int(*new_sides) > 0:
                    self._Figure__sides = list(new_sides)
                    self.__radius = self._Figure__sides[0] / (2 * pi)

    def get_square(self):
        """
        Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        """
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        """
        Все атрибуты и методы класса Figure
        """
        Figure.__init__(self, color, *sides, filled=False)
        if self.__is_valid_sides(sides):
            self._Figure__sides = list(sides)
        else:
            self._Figure__sides = [1] * self.sides_count

    def __is_valid_sides(self, sides):
        """
        Переопределяет __is_valid_sides, выполняет проверку на "Неравенство треугольника".
        "Длина любой стороны треугольника всегда меньше суммы длин двух других сторон".
        """
        if len(sides) == 3:
            for every_side in list(sides):
                if isinstance(every_side, int):
                    if every_side <= 0:
                        return False
                    else:
                        a = sides[0]
                        b = sides[1]
                        c = sides[2]
                        if a < (b + c) and b < (a + c) and c < (a + b):
                            return True
                        else:
                            return False
                else:
                    return False
        else:
            return False

    def get_square(self):
        """
        Метод get_square возвращает площадь треугольника.
        """
        a = self._Figure__sides[0]
        b = self._Figure__sides[1]
        c = self._Figure__sides[2]
        p = 0.5 * sum(self._Figure__sides)
        """
        Можно рассчитать по формуле Герона:
        p = 0.5*(a + b + c)
        S^2 = p(p - a)(p - b)(p - c)
        """
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        """
        Все атрибуты и методы класса Figure
        """
        Figure.__init__(self, color, *sides, filled=False)
        self.set_sides(*sides)

    def set_sides(self, *new_sides):
        """
        Переопределяет _Figure__sides, создавая список из 12 одинаковы сторон (передаётся 1 сторона)
        """
        if len(new_sides) == 1:
            if isinstance(*new_sides, int):
                if int(*new_sides) > 0:
                    self._Figure__sides = [*new_sides] * self.sides_count

    def get_volume(self):
        """
        Метод get_volume, возвращает объём куба.
        """
        return self._Figure__sides[0] ** 3


if __name__ == '__main__':

    def test(any_obj):
        global num_line
        print('|--------------------------------------------------')
        print(f'|  "Test {num_line}  --> {any_obj.__class__.__name__}"')
        atr_dict = any_obj.__dict__.copy()
        for key in atr_dict:
            print(f"| {key}  --> {atr_dict.get(key)}")
        num_line += 1


    num_line = 1

    print('\n|-------------------------  <<< My.Test.CODE >>>  -------------------------')
    print(f'\n| _________________________{Figure}_________________________\n')
    x = Figure((0, 0, 255), 100)  # True
    test(x)

    x = Figure((-1, 0, 255), -3)  # False
    test(x)

    x = Figure((000, 111, 222), 555)  # True
    test(x)

    x.set_color(55, 66, 77)  # Изменится
    x.set_sides(10, 20, 30)
    test(x)

    x.set_color(300, 70, 15)  # Не изменится
    x.set_sides(-44)
    test(x)  # |  Test 5     --> Figure

    num_line = 1
    print('|_________________________________________________________________________________|')

    print(f'\n| _________________________{Circle}_________________________\n')


    def test_circle(any_obj):
        test(any_obj)
        print(f"| .get_square()   --> {x.get_square()}")


    x = Circle((-10, 10, 10), 5, 3, 1)  # False
    test_circle(x)

    x = Circle((-1, 0, 255), -3)  # False
    test_circle(x)

    x = Circle((000, 111, 222), 3, 3, 3)  # False
    test_circle(x)

    x = Circle((000, 111, 222), 555)  # True
    test_circle(x)

    x.set_color(55, 66, 77)  # Изменится
    x.set_sides(302)
    test_circle(x)

    x.set_color(300, 70, 15)  # Не изменится
    x.set_sides(-44)
    test_circle(x)

    num_line = 1
    print('|_________________________________________________________________________________|')

    print(f'\n| _________________________{Triangle}_________________________\n')


    def test_triangle(any_obj):
        test(any_obj)
        print(f"| .get_square()   --> {x.get_square()}")


    x = Triangle((-10, 10, 10), 5, 3, 1)  # False
    test_triangle(x)

    x = Triangle((-1, 0, 255), -3)  # False
    test_triangle(x)

    x = Triangle((000, 111, 222), 555)  # False
    test_triangle(x)

    x = Triangle((000, 111, 222), 5, 5, 5)  # True
    test_triangle(x)

    x.set_color(55, 66, 77)  # Изменится
    x.set_sides(11, 21, 31)
    test_triangle(x)

    x.set_color(300, 70, 15)  # Не изменится
    x.set_sides(-44)
    test_triangle(x)

    num_line = 1
    print('|_________________________________________________________________________________|')

    print(f'\n| _________________________{Cube}_________________________\n')


    def test_cube(any_obj):
        test(any_obj)
        print(f"| .get_volume()   --> {x.get_volume()}")


    x = Cube((-1, 0, 255), -3)  # False
    test_cube(x)

    x = Cube((000, 111, 222), 555, 45, 28)  # False
    test_cube(x)

    x = Cube((0, 0, 255), 100)  # True
    test_cube(x)

    x.set_color(55, 66, 77)  # Изменится
    x.set_sides(420)
    test_cube(x)

    x.set_color(300, 70, 15)  # Не изменится
    x.set_sides(-44)
    test_cube(x)

    num_line = 1
    print('|_________________________________________________________________________________|')

    #

    print('\n     -------------  <<< URBAN.TEST.CODE >>>  -------------\n')
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
