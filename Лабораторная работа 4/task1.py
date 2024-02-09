from math import sqrt
from typing import Union

""" Значения-константы границ доски, используемых в классе Point2D """
RIGHT_BORDER_X = 100
LEFT_BORDER_X = -100
TOP_BORDER_Y = 100
BOTTOM_BORDER_Y = -100


class Point2D:
    """
    Документация на класс Point2D.
    Класс описывает модель точки в 2-х мерном пространстве.
    """

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float]):
        """ Инициализация экземпляра класса.
        :param coordinate_x: Координата x точки.
        :param coordinate_y: Координата y точки.
        """
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y

    def calculate_distance_to_0(self) -> float:
        """ Метод просчитывает и возвращает расстояние до нуля. """
        return sqrt(self.coordinate_y ** 2 + self.coordinate_x ** 2)

    def calculate_distance_to_point(self, point) -> float:
        """
        Метод просчитывает и возвращает расстояние до другой точки.
        :param point: Точка, до которой просчитывается расстояние.
        """
        if not isinstance(point, Point2D):
            raise TypeError("Wrong type of other point")
        distance_x = self.coordinate_x - point.coordinate_x
        distance_y = self.coordinate_y - point.coordinate_y
        return sqrt(distance_x ** 2 + distance_y ** 2)

    @property
    def coordinate_x(self) -> Union[int, float]:
        """ Getter для координаты x. """
        return self._coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, new_x_coordinate: int) -> None:
        """ Setter для координаты x. """
        if not isinstance(new_x_coordinate, (int, float)):
            raise TypeError("Wrong type of coordinate_x")
        if new_x_coordinate > RIGHT_BORDER_X or new_x_coordinate < LEFT_BORDER_X:
            raise ValueError("coordinate_x is out of borders")
        self._coordinate_x = new_x_coordinate
        self.calculate_distance_to_0()

    @property
    def coordinate_y(self) -> Union[int, float]:
        """ Getter для координаты y. """
        return self._coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, new_y_coordinate: int) -> None:
        """ Setter для координаты y. """
        if not isinstance(new_y_coordinate, (int, float)):
            raise TypeError("Wrong type of coordinate_y")
        if new_y_coordinate > TOP_BORDER_Y or new_y_coordinate < BOTTOM_BORDER_Y:
            raise ValueError("coordinate_y is out of borders")
        self._coordinate_y = new_y_coordinate
        self.calculate_distance_to_0()

    def __str__(self):
        return f"Точка({self._coordinate_x}, {self._coordinate_y})"

    def __repr__(self):
        return f"{self.__class__.__name__}(coordinate_x={self._coordinate_x}, coordinate_y={self._coordinate_y})"


class Polygon2D:
    """
    Документация на базовый класс Polygon2D.
    Дочерние классы: Triangle2D, Quadrangle2D.
    Класс описывает модель многогранника в 2-х мерном пространстве.
    """

    def __init__(self, points: list[Point2D] = None):
        """
        Инициализация экземпляра класса.
        В дочерних классах наследуется
        :param points: Список точек класса Point2D.
        """
        self.points = points

    def number_of_points(self) -> int:
        """
        Метод просчитывает и возвращает кол-во точек в многоугольнике.
        Метод наследуется всеми дочерними классами
        """
        return len(self._points)

    def perimeter(self) -> float:
        """
        Метод просчитывает и возвращает длину периметра в многоугольнике.
        Метод перегружается всеми дочерними классами
        """
        result = self._points[-1].calculate_distance_to_point(self._points[0])
        for i, point in enumerate(self._points[:-1:]):
            result += point.calculate_distance_to_point(self._points[i + 1])
        return result

    @property
    def points(self) -> list[Point2D]:
        """ Getter для списка точек. """
        return self._points

    @points.setter
    def points(self, new_points: list[Point2D]) -> None:
        """
        Setter для списка точек.
        В дочерних классах перегружается
        """
        if new_points is None:
            self._points = []
        else:
            if not isinstance(new_points, list):
                raise TypeError("Wrong type of points, must be list")
            for point in new_points:
                if not isinstance(point, Point2D):
                    raise TypeError("Wrong type of point, must be class Point2D")
            self._points = new_points

    def __str__(self):
        """
        Магический метод __str__
        В дочерних классах перегружается
        """
        points_str = map(lambda point: point.__str__(), self._points)
        return f"Многоугольник. Точки: {list(points_str)}"

    def __repr__(self):
        """
        Магический метод __repr__
        В дочерних классах наследуется
        """
        return f"{self.__class__.__name__}(points={self._points})"


class Triangle2D(Polygon2D):
    """
    Документация на дочерний класс Triangle2D.
    Базовый класс: Polygon2D.
    Класс описывает модель треугольника в 2-х мерном пространстве.
    """

    def perimeter(self) -> float:
        """
        Метод просчитывает и возвращает длину периметра в треугольнике.
        Метод перегружается для избавления от цикла.
        """
        result = self._points[0].calculate_distance_to_point(self._points[1])
        result += self._points[1].calculate_distance_to_point(self._points[2])
        result += self._points[2].calculate_distance_to_point(self._points[0])
        return result

    @property
    def points(self) -> list[Point2D]:
        """ Getter для списка точек треугольника. """
        return self._points

    @points.setter
    def points(self, new_points: list[Point2D]) -> None:
        """
        Setter для списка точек треугольника.
        Перегружаем для проверки кол-ва точек.
        """
        if len(new_points) != 3:
            raise IndexError("Number of points in triangle must be 3")
        else:
            if not isinstance(new_points, list):
                raise TypeError("Wrong type of points, must be list")
            for point in new_points:
                if not isinstance(point, Point2D):
                    raise TypeError("Wrong type of point, must be class Point2D")
            self._points = new_points

    def __str__(self):
        """
        Магический метод __str__
        Перегружаем, так как изменилось название с многоугольника на треугольник
        """
        points_str = map(lambda point: point.__str__(), self._points)
        return f"Треугольник. Точки: {list(points_str)}"


class Quadrangle2D(Polygon2D):
    """
    Документация на дочерний класс Quadrangle2D.
    Базовый класс: Polygon2D.
    Класс описывает модель четырёхугольника в 2-х мерном пространстве.
    """

    def perimeter(self) -> float:
        """
        Метод просчитывает и возвращает длину периметра в четырёхугольнике.
        Метод перегружается для избавления от цикла.
        """
        result = self._points[0].calculate_distance_to_point(self._points[1])
        result += self._points[1].calculate_distance_to_point(self._points[2])
        result += self._points[2].calculate_distance_to_point(self._points[3])
        result += self._points[3].calculate_distance_to_point(self._points[0])
        return result

    @property
    def points(self) -> list[Point2D]:
        """ Getter для списка точек треугольника. """
        return self._points

    @points.setter
    def points(self, new_points: list[Point2D]) -> None:
        """
        Setter для списка точек четырёхугольника.
        Перегружаем для проверки кол-ва точек.
        """
        if len(new_points) != 4:
            raise IndexError("Number of points in triangle must be 3")
        else:
            if not isinstance(new_points, list):
                raise TypeError("Wrong type of points, must be list")
            for point in new_points:
                if not isinstance(point, Point2D):
                    raise TypeError("Wrong type of point, must be class Point2D")
            self._points = new_points

    def __str__(self):
        """
        Магический метод __str__
        Перегружаем, так как изменилось название с многоугольника на четырёхугольник
        """
        points_str = map(lambda point: point.__str__(), self._points)
        return f"Четырёхугольник. Точки: {list(points_str)}"


if __name__ == "__main__":
    """ Пример использования классов """
    point1 = Point2D(0, 0)
    point2 = Point2D(0, 1)
    point3 = Point2D(1, 1)
    point4 = Point2D(1, 0)
    figure1 = Triangle2D([point1, point2, point3])
    figure2 = Quadrangle2D([point1, point2, point3, point4])
    print(figure1)
    print("Кол-во точек: ", figure1.number_of_points())
    print("Длина периметра: ", figure1.perimeter())
    print(figure2)
    print("Кол-во точек: ", figure2.number_of_points())
    print("Длина периметра: ", figure2.perimeter())
