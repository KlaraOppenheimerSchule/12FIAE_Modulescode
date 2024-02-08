import abc

# Interface ChangeListener
class ChangeListener(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass


    
