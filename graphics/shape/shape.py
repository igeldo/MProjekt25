from abc import ABC, abstractmethod

from graphics.base.point import Point
from graphics.base.util import check_type
from graphics.plot.plot import Plot


class Shape(ABC):
    def __init__(self, center: Point) -> None:
        self._center = check_type(center, Point, 'center')

    def get_center(self) -> Point:
        return self._center

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def plot(self, plot: Plot) -> None:
        pass
