from classes.classifiers import AbstractClassifier


class Square(AbstractClassifier):
    def match(self, curve):
        if len(curve) != 4:
            return False

        # TODO: check lines 1 and 3 (2 and 4) is parallel

        # TODO: check lines have same length

        return False

