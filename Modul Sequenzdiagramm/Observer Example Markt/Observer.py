import abc

# Interface Observer
class Observer(metaclass=abc.ABCMeta):

    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    @abc.abstractmethod
    def update(self):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass