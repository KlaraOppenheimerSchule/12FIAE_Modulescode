from abc import ABCMeta, abstractmethod

class SearchAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def runAlgorithm(self, array, value):
        pass
