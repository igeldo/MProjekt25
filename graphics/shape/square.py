from graphics.base.point import Point
from graphics.shape.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, center: Point, width: float) -> None:
        super().__init__(center, width, width)

    def __str__(self) -> str:
        return f"Square({self.get_center()},{self.get_width()})"
