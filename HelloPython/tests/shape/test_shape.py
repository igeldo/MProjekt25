from unittest import TestCase

from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class ShapeForTest(Shape):

    def __init__(self, center: Point):
        super().__init__(center)

    def calculate_area(self) -> float:
        pass

    def plot(self, plot: Plot) -> None:
        pass


class TestShape(TestCase):

    def test_init_fails_for_wrong_center_type(self):
        # arrange
        center = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, '^center can only be a Point$'):
            ShapeForTest(center)

    def test_get_center(self):
        # arrange
        cut = ShapeForTest(Point(1, 2))

        # act
        result = cut.get_center()

        # assert
        self.assertEqual(Point(1, 2), result)
