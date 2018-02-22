from classes.classifiers import AbstractClassifier
from geometry_util import direction_change


class Circle(AbstractClassifier):
    def match(self, curve):
        if len(curve) < 5:
            return False
        turn_to = None
        for i in range(0, len(curve) - 3):
            point0 = curve[i + 0][0]
            point1 = curve[i + 1][0]
            point2 = curve[i + 2][0]
            t = direction_change(
                point0[0], point0[1],
                point1[0], point1[1],
                point2[0], point2[1],
            )
            if turn_to is not None and t != turn_to:
                return False
            if turn_to is None:
                turn_to = t
            pass

        return True  # TODO: implement me!!
