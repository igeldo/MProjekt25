from math import isclose
from unittest import TestCase
from unittest.mock import Mock

from graphics.base.point import Point
from graphics.shape.circle import Circle


class TestCircle(TestCase):

    def setUp(self):
        self.center = Point(1, 2)
        self.cut = Circle(self.center, 3)

    def test_init_fails_for_wrong_radius_type(self):
        # arrange
        radius = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, '^radius can only be a float or int$'):
            Circle(self.center, radius)

    def test_init_fails_for_negative_radius(self):
        # arrange
        radius = -4

        # act & assert
        with self.assertRaisesRegex(ValueError, '^radius must be greater than zero$'):
            Circle(self.center, radius)

    def test_get_center(self):
        # act
        result = self.cut.get_center()

        # assert
        self.assertEqual(Point(1, 2), result)

    def test_get_radius(self):
        # act
        result = self.cut.get_radius()

        # assert
        self.assertEqual(3, result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertTrue(isclose(28.274333882308139, result))

    def test_calculate_area_using_equal(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(28.274333882308139, result)

    def test_plot(self):
        # arrange
        plot = Mock()

        # act
        self.cut.plot(plot)

        # assert
        plot.plot_circle.assert_called_once_with(Point(1, 2), 3, 'red')

    def test_plot_with_color(self):
        # arrange
        plot = Mock()

        # act
        self.cut.plot(plot, 'someColor')

        # assert
        plot.plot_circle.assert_called_once_with(Point(1, 2), 3, 'someColor')

    def test_str(self):
        # act
        result = str(self.cut)

        # assert
        self.assertEqual("Circle(Point(1.0,2.0),3.0)", result)
