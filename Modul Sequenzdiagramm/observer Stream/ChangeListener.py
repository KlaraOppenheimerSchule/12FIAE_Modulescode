import abc

class ChangeListener(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass


    
