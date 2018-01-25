__author__ = 'GoForBroke'

from abc import ABCMeta, abstractmethod


class AbstractClassifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def match(self, curve):
        # type: (list) -> bool
        pass
