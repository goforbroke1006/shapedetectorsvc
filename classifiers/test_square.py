from unittest import TestCase

from classifiers.Square import Square


class TestSquare(TestCase):
    def test_match(self):
        examples = (
            (
                ((0, 0), (10, 0), (10, 10), (0, 10)),
                True,
            ),
            (
                ((2, 1), (2, 4), (-1, 4), (-1, -1)),
                True,
            ),
            (
                ((1, 1), (1, -1), (-1, -1), (-1, 1)),
                True,
            ),
            (
                ((0, 0), (10, 0), (10, 10)),
                False,
            ),
            (
                ((0, 2), (10, 0), (10, 10), (0, 10)),
                False,
            ),
        )

        classifier = Square()

        for curve, result in examples:
            if classifier.match(curve) != result:
                self.fail(", ".join("(%s, %s)" % (el[0], el[1]) for el in curve)
                          + " should be %sa " % ("" if result else "not ")
                          + classifier.__class__.__name__)
