import matplotlib.pyplot as plt
from matplotlib import patches

from graphics.base.point import Point


class Plot:

    def __init__(self):
        self._fig, self._ax = plt.subplots()
        self._ax.set_xlim(-1, 21)
        self._ax.set_ylim(-1, 21)
        plt.axis('square')

    def plot_line(self, p1: Point, p2: Point) -> None:
        plt.plot([p1.get_x(), p2.get_x()], [p1.get_y(), p2.get_y()])

    def plot_rectangle(self, corner: Point, width: float, height: float, color: str) -> None:
        self._ax.add_patch(
            patches.Rectangle(
                (corner.get_x(), corner.get_y()),
                width,
                height,
                color = color
            )
        )

    def plot_triangle(self, p1: Point, p2: Point, p3: Point, color: str) -> None:
        self._ax.add_patch(
            patches.Polygon((
                (p1.get_x(), p1.get_y()),
                (p2.get_x(), p2.get_y()),
                (p3.get_x(), p3.get_y())
            ),
                color = color
            )
        )

    def plot_circle(self, center: Point, radius: float, color: str) -> None:
        self._ax.add_patch(
            patches.Circle(
                (center.get_x(), center.get_y()),
                radius,
                color = color
            )
        )

    def show(self):
        plt.show()
