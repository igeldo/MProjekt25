from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.square import Square


class TestSquare(TestCase):

    def setUp(self):
        self.cut = Square(Point(1, 2), 3)

    def test_get_width(self):
        # act
        result = self.cut.get_width()

        # assert
        self.assertEqual(3, result)

    def test_get_height(self):
        # act
        result = self.cut.get_height()

        # assert
        self.assertEqual(3, result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(9, result)

    def test_str(self):
        # act
        result = str(self.cut)

        # assert
        self.assertEqual("Square(Point(1.0,2.0),3.0)", result)
