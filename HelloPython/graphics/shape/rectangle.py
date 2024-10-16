from graphics.base.point import Point
from graphics.base.util import check_float_positive
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Rectangle(Shape):

    def __init__(self, center: Point, width: float, height: float) -> None:
        super().__init__(center)
        self._width = check_float_positive(width, 'width')
        self._height = check_float_positive(height, 'height')
        self._p1 = Point(self.get_center().get_x() - width / 2, self.get_center().get_y() - height / 2)
        self._p2 = Point(self.get_center().get_x() + width / 2, self.get_center().get_y() - height / 2)
        self._p3 = Point(self.get_center().get_x() + width / 2, self.get_center().get_y() + height / 2)
        self._p4 = Point(self.get_center().get_x() - width / 2, self.get_center().get_y() + height / 2)

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def calculate_area(self) -> float:
        return self._width * self._height

    def plot(self, plot: Plot, color: str = 'green') -> None:
        plot.plot_rectangle(self._p1, self._width, self._height, color)

    def __str__(self) -> str:
        return f"Rectangle({self.get_center()},{self.get_width()},{self.get_height()})"
