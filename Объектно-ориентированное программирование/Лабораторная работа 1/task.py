import doctest
from math import sqrt
from typing import Union

""" Значения-константы границ доски, используемых в классах """
RIGHT_BORDER_X = 100
LEFT_BORDER_X = -100
TOP_BORDER_Y = 100
BOTTOM_BORDER_Y = -100

""" Значения математических постоянных, используемых в классах """
PI = 3.14


class Point2D:
    """
    Документация на класс Point2D.
    Класс описывает модель точки в 2-х мерном пространстве.
    """

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float]):
        """ Инициализация экземпляра класса.
        :param coordinate_x: Координата x точки.
        :param coordinate_y: Координата y точки.

        Пример:
        >>> point = Point2D(0,10) # инициализация класса
        >>> point.distance_to_0 # расстояние до нуля
        10.0
        """
        self.coordinate_x = None
        self.init_coordinate_x(coordinate_x)

        self.coordinate_y = None
        self.init_coordinate_y(coordinate_y)

        self.distance_to_0 = None
        self.init_distance_to_0()

    def init_coordinate_x(self, coordinate_x: Union[int, float]):
        """ Инициализация координаты x. """
        if not isinstance(coordinate_x, (int, float)):
            raise TypeError("Wrong type of coordinate_x")
        if coordinate_x > RIGHT_BORDER_X or coordinate_x < LEFT_BORDER_X:
            raise ValueError("coordinate_x is out of borders")
        self.coordinate_x = coordinate_x

    def init_coordinate_y(self, coordinate_y: Union[int, float]):
        """ Инициализация координаты y. """
        if not isinstance(coordinate_y, (int, float)):
            raise TypeError("Wrong type of coordinate_y")
        if coordinate_y > TOP_BORDER_Y or coordinate_y < BOTTOM_BORDER_Y:
            raise ValueError("coordinate_y is out of borders")
        self.coordinate_y = coordinate_y

    def init_distance_to_0(self):
        """ Инициализация расстояния до (0,0). """
        self.distance_to_0 = sqrt(self.coordinate_y ** 2 + self.coordinate_x ** 2)

    def calculate_distance_to_point(self, point) -> float:
        """
        Метод просчитывает и возвращает расстояние до другой точки.
        :param point: Точка, до которой просчитывается расстояние.

        Примеры использования метода:
        >>> Point2D(10, 0).calculate_distance_to_point(Point2D(5, 0))
        5.0
        >>> Point2D(0, 100).calculate_distance_to_point(Point2D(0, 50))
        50.0
        """
        if not isinstance(point, Point2D):
            raise TypeError("Wrong type of other point")
        distance_x = self.coordinate_x - point.coordinate_x
        distance_y = self.coordinate_y - point.coordinate_y
        return sqrt(distance_x ** 2 + distance_y ** 2)

    def calculate_distance_to_line(self, line) -> float:
        """
        Метод просчитывает и возвращает расстояние до отрезка.
        :param line: Отрезок, до которого просчитывается расстояние.

        Пример использования метода:
        >>> Point2D(10, 0).calculate_distance_to_line(Line2D(Point2D(5,0), Point2D(0,5)))
        0.0
        """
        if not isinstance(line, Line2D):
            raise TypeError("Wrong type of line")
        return 0.0

    def is_on_line(self, line) -> bool:
        """
        Метод указывает, находится ли точка на отрезке.
        :param line: Отрезок, который проверяется.

        Пример использования метода:
        >>> Point2D(10, 0).is_on_line(Line2D(Point2D(5,0), Point2D(0,5)))
        False
        """
        if not isinstance(line, Line2D):
            raise TypeError("Wrong type of line")
        return False

    def is_on_circle(self, circle) -> bool:
        """
        Метод указывает, находится ли точка на окружности.
        :param circle: Круг, который проверяется.

        Пример использования метода:
        >>> Point2D(10, 0).is_on_circle(Circle2D(Point2D(5,0), 5))
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False

    def is_inside_circle(self, circle) -> bool:
        """
        Метод указывает, находится ли точка внутри круга.
        :param circle: Круг, которая проверяется.

        Пример использования метода:
        >>> Point2D(10, 0).is_inside_circle(Circle2D(Point2D(5,0), 5))
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False


class Line2D:
    """
    Документация на класс Line2D.
    Класс описывает модель отрезка в 2-х мерном пространстве.
    """

    def __init__(self, point_a: Point2D, point_b: Point2D):
        """ Инициализация экземпляра класса.
        :param point_a: Точка а.
        :param point_b: Точка b.

        Пример:
        >>> line = Line2D(Point2D(0,10), Point2D(0,20)) # инициализация класса
        >>> line.length # длина отрезка
        10.0
        """
        self.point_a = None
        self.init_point(point_a, 'a')

        self.point_b = None
        self.init_point(point_b, 'b')

        self.length = None
        self.init_length()

    def init_point(self, point: Point2D, name: str):
        """ Инициализация точек отрезка. """
        if not isinstance(point, Point2D):
            raise TypeError("Wrong type of point_", name)
        if name not in ['a', 'b']:
            raise ValueError("Wrong name of point")
        if name == 'a':
            self.point_a = point
        else:
            self.point_b = point

    def init_length(self):
        """ Инициализация длины отрезка. """
        self.length = self.point_a.calculate_distance_to_point(self.point_b)

    def calculate_distance_to_point(self, point: Point2D) -> float:
        """
        Метод просчитывает и возвращает расстояние до точки.
        :param point: Точка, до которой просчитывается расстояние.

        Пример использования метода:
        >>> line = Line2D(Point2D(0,10), Point2D(0,20))
        >>> line.calculate_distance_to_point(Point2D(5,0))
        0.0
        """
        if not isinstance(point, Point2D):
            raise TypeError("Wrong type of other point")
        return 0.0

    def calculate_distance_to_line(self, line) -> float:
        """
        Метод просчитывает и возвращает расстояние до отрезка.
        :param line: Отрезок, до которого просчитывается расстояние.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> line2 = Line2D(Point2D(1,10), Point2D(1,20))
        >>> line1.calculate_distance_to_line(line2)
        0.0
        """
        if not isinstance(line, Line2D):
            raise TypeError("Wrong type of line")
        return 0.0

    def has_point(self, other_point: Point2D) -> bool:
        """
        Метод указывает, находится ли точка на отрезке.
        :param other_point: Точка, которая проверяется.

        Пример использования метода:
        >>> line = Line2D(Point2D(0,10), Point2D(0,20))
        >>> line.has_point(Point2D(5,0))
        False
        """
        if not isinstance(other_point, Point2D):
            raise TypeError("Wrong type of other point")
        return False

    def does_cross_line(self, line) -> bool:
        """
        Метод указывает, пересекает ли отрезок другой отрезок.
        :param line: Отрезок, который проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> line2 = Line2D(Point2D(1,10), Point2D(1,20))
        >>> line1.does_cross_line(line2)
        False
        """
        if not isinstance(line, Line2D):
            raise TypeError("Wrong type of line")
        return False

    def is_inside_circle(self, circle) -> bool:
        """
        Метод указывает, находится ли отрезок внутри окружности.
        :param circle: Круг, которая проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> line1.is_inside_circle(circle1)
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False

    def is_chord(self, circle) -> bool:
        """
        Метод указывает, является ли отрезок хордой окружности.
        :param circle: Круг, которая проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> line1.is_chord(circle1)
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False

    def is_diameter(self, circle) -> bool:
        """
        Метод указывает, является ли отрезок диаметром окружности.
        :param circle: Круг, которая проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> line1.is_diameter(circle1)
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False

    def is_radius(self, circle) -> bool:
        """
        Метод указывает, является ли отрезок радиусом окружности.
        :param circle: Круг, которая проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> line1.is_radius(circle1)
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False


class Circle2D:
    """
    Документация на класс Circle2D.
    Класс описывает модель круга в 2-х мерном пространстве.
    """

    def __init__(self, center: Point2D, radius: Union[int, float]):
        """ Инициализация экземпляра класса.
        :param center: Точка-центр круга.
        :param radius: Длина радиуса круга.

        Пример:
        >>> circe = Circle2D(Point2D(10,0), 10) # инициализация класса
        >>> circe.diameter # диаметр круга
        20
        >>> circe.perimetr # диаметр круга
        62.800000000000004
        >>> circe.area # диаметр круга
        314.0
        """
        self.center = None
        self.init_center(center)

        self.radius = None
        self.init_radius(radius)

        self.diameter = None
        self.init_diameter()

        self.perimetr = None
        self.init_perimetr()

        self.area = None
        self.init_area()

    def init_center(self, center: Point2D):
        """ Инициализация точки-центра круга. """
        if not isinstance(center, Point2D):
            raise TypeError("Wrong type of center point")
        self.center = center

    def init_radius(self, radius: Union[int, float]):
        """ Инициализация длины радиуса круга. """
        if not isinstance(radius, (int, float)):
            raise TypeError("Wrong type of radius")
        if radius <= 0:
            raise ValueError("Radius can't be 0 or less")
        if self.center.coordinate_x + radius > RIGHT_BORDER_X \
                or self.center.coordinate_x - radius < LEFT_BORDER_X \
                or self.center.coordinate_y + radius > TOP_BORDER_Y \
                or self.center.coordinate_y - radius < BOTTOM_BORDER_Y:
            raise ValueError("Circle is out of borders")
        self.radius = radius

    def init_diameter(self):
        """ Инициализация длины диаметра круга. """
        self.diameter = 2 * self.radius

    def init_perimetr(self):
        """ Инициализация периметра круга. """
        self.perimetr = self.diameter * PI

    def init_area(self):
        """ Инициализация периметра круга. """
        self.area = self.radius**2 * PI

    def has_point_on(self, other_point: Point2D) -> bool:
        """
        Метод указывает, находится ли точка на окружности.
        :param other_point: Точка, которая проверяется.

        Пример использования метода:
        >>> point1 = Point2D(0,10)
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> circle1.has_point_on(point1)
        False
        """
        if not isinstance(other_point, Point2D):
            raise TypeError("Wrong type of other point")
        return False

    def has_point_inside(self, other_point: Point2D) -> bool:
        """
        Метод указывает, находится ли точка внутри круга.
        :param other_point: Точка, которая проверяется.

        Пример использования метода:
        >>> point1 = Point2D(0,10)
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> circle1.has_point_inside(point1)
        False
        """
        if not isinstance(other_point, Point2D):
            raise TypeError("Wrong type of other point")
        return False

    def has_line_inside(self, line: Line2D) -> bool:
        """
        Метод указывает, есть ли внутри круга отрезок.
        :param line: Отрезок, который проверяется.

        Пример использования метода:
        >>> line1 = Line2D(Point2D(0,10), Point2D(0,20))
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> circle1.has_line_inside(line1)
        False
        """
        if not isinstance(line, Line2D):
            raise TypeError("Wrong type of line")
        return False

    def does_cross_circle(self, circle) -> bool:
        """
        Метод указывает, пересекает ли окружность другую окружность.
        :param circle: Круг, который проверяется.

        Пример использования метода:
        >>> circle1 = Circle2D(Point2D(1,10), 5)
        >>> circle2 = Circle2D(Point2D(2,15), 5)
        >>> circle1.does_cross_circle(circle2)
        False
        """
        if not isinstance(circle, Circle2D):
            raise TypeError("Wrong type of circle")
        return False


if __name__ == "__main__":
    doctest.testmod()
