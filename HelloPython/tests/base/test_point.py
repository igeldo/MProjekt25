from unittest import TestCase

from graphics.base.point import Point
from graphics.base.vector import Vector


class TestPoint(TestCase):

    def setUp(self):
        self.cut = Point(2, 3)

    def test_str(self):
        # act
        result = str(self.cut)

        # assert
        self.assertEqual("Point(2.0,3.0)", result)

    def test_add_succeeds_for_vector(self):
        # arrange
        other: Vector = Vector(4, 5)

        # act
        result = self.cut + other

        # assert
        self.assertEqual(Point(6, 8), result)

    def test_add_fails_for_point(self):
        # arrange
        other: Point = Point(4, 5)

        # act & assert
        with self.assertRaisesRegex(TypeError, '^other can only be a Vector$'):
            self.cut + other
