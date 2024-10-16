from unittest import TestCase

from graphics.base.point import Point
from graphics.base.vector import Vector


class TestVector(TestCase):

    def setUp(self):
        self.cut = Vector(5, 6)

    def test_str(self):
        # act
        result = str(self.cut)

        # assert
        self.assertEqual("Vector(5.0,6.0)", result)

    def test_add_succeeds_for_vector(self):
        # act
        other = Vector(4, 5)

        # act
        result = self.cut + other

        # assert
        self.assertEqual(Vector(9, 11), result)

    def test_add_fails_for_point(self):
        # act
        other = Point(4, 5)

        # act & assert
        with self.assertRaisesRegex(TypeError, '^other can only be a Vector$'):
            self.cut + other
