from __future__ import annotations

from graphics.base.coordinate2d import Coordinate2D
from graphics.base.util import check_type


class Vector(Coordinate2D):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Vector({self._x},{self._y})"

    def __add__(self, other) -> Vector:
        check_type(other, Vector, 'other')
        return Vector(self.get_x() + other.get_x(), self.get_y() + other.get_y())
