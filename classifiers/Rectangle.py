from classes.classifiers import AbstractClassifier


class Rectangle(AbstractClassifier):
    def match(self, curve):
        if len(curve) != 4:
            return False

        # TODO: check line 1 and 3 (2 and 4) is parallel

        return False

