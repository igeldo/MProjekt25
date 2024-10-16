from graphics.base.point import Point
from graphics.base.util import check_type
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Triangle(Shape):

    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        self._p1 = check_type(p1, Point, 'p1')
        self._p2 = check_type(p2, Point, 'p2')
        self._p3 = check_type(p3, Point, 'p3')
        super().__init__(
            Point(
                (p1.get_x() + p2.get_x() + p3.get_x()) / 3,
                (p1.get_y() + p2.get_y() + p3.get_y()) / 3
            )
        )

    def calculate_area(self) -> float:
        return (
                self._p1.get_x() * (self._p2.get_y() - self._p3.get_y())
                + self._p2.get_x() * (self._p3.get_y() - self._p1.get_y())
                + self._p3.get_x() * (self._p1.get_y() - self._p2.get_y())
        ) / 2

    def plot(self, plot: Plot, color: str = 'blue') -> None:
        plot.plot_triangle(self._p1, self._p2, self._p3, color)

    def __str__(self) -> str:
        return f"Triangle({self._p1},{self._p2},{self._p3})"
