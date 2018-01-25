from classes.classifiers import AbstractClassifier


class Triangle(AbstractClassifier):
    def match(self, curve):
        return len(curve) == 3
