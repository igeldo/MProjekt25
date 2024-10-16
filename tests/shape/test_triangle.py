from unittest import TestCase
from unittest.mock import Mock

from graphics.base.point import Point
from graphics.shape.triangle import Triangle


class TestTriangle(TestCase):

    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(9, 0)
        self.p3 = Point(0, 6)
        self.cut = Triangle(p1=self.p1, p2=self.p2, p3=self.p3)

    def test_init_fails_for_wrong_p1_type(self):
        # arrange
        p1 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, '^p1 can only be a Point$'):
            Triangle(p1=p1, p2=self.p2, p3=self.p3)

    def test_init_fails_for_wrong_p2_type(self):
        # arrange
        p2 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, '^p2 can only be a Point$'):
            Triangle(p1=self.p1, p2=p2, p3=self.p3)

    def test_init_fails_for_wrong_p3_type(self):
        # arrange
        p3 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, '^p3 can only be a Point$'):
            Triangle(p1=self.p1, p2=self.p2, p3=p3)

    def test_get_center(self):
        # act
        result = self.cut.get_center()

        # assert
        self.assertEqual(Point(3, 2), result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(27, result)

    def test_plot(self):
        # arrange
        plot = Mock()

        # act
        self.cut.plot(plot)

        # assert
        plot.plot_triangle.assert_called_once_with(self.p1, self.p2, self.p3, 'blue')

    def test_plot_with_color(self):
        # arrange
        plot = Mock()

        # act
        self.cut.plot(plot, 'someColor')

        # assert
        plot.plot_triangle.assert_called_once_with(self.p1, self.p2, self.p3, 'someColor')

    def test_str(self):
        # act
        result = str(self.cut)

        # assert
        self.assertEqual("Triangle(Point(0.0,0.0),Point(9.0,0.0),Point(0.0,6.0))", result)
