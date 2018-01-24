from unittest import TestCase
import geometry_util


class TestGeometryUtil(TestCase):
    def test_vector_rotation(self):
        angle = geometry_util.vectors_angle(0, 0, 4, 4)
        if angle != 45:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

        angle = geometry_util.vectors_angle(0, 0, 100, 173.206)
        if angle != 60:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

        angle = geometry_util.vectors_angle(2, -2, 0, 0)
        if angle != 135:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

        angle = geometry_util.vectors_angle(10, -3, 5, 2)
        if angle != 135:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

        angle = geometry_util.vectors_angle(10, -3, -10, -3)
        if angle != 180:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

        angle = geometry_util.vectors_angle(2, -2, 0, -4)
        if angle != 180 + 45:
            self.fail("Unexpected vector rotation angle from abscissa: %f" % angle)

    def test_direction_change(self):

        d = geometry_util.direction_change(0, 0, 100, 173.2, 104, 177.2)
        if d != geometry_util.DIRECTION_RIGHT:
            self.fail()

        d = geometry_util.direction_change(0, 0, 4, 4, 104, 177.2)
        if d != geometry_util.DIRECTION_LEFT:
            self.fail()

        d = geometry_util.direction_change(8, -1, 10, -3, 8, 9)
        if d != geometry_util.DIRECTION_LEFT:
            self.fail()

        d = geometry_util.direction_change(2, -2, 0, -4, -5, -1)
        if d != geometry_util.DIRECTION_RIGHT:
            self.fail()

        d = geometry_util.direction_change(2, -2, 0, -4, -5, 1)
        if d != geometry_util.DIRECTION_RIGHT:
            self.fail()
