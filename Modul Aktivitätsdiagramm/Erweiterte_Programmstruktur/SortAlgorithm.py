from abc import ABCMeta, abstractmethod

class SortAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def runAlgorithm(self, array):
        pass
