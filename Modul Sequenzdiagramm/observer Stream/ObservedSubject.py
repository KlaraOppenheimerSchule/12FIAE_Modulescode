import abc
from ChangeListener import ChangeListener


# Interface ObservedSubject
class ObservedSubject(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod 
    def addChangeListener(changeListener : ChangeListener):
        pass
    
    @abc.abstractmethod 
    def removeChangeListener(changeListener : ChangeListener):
        pass
    
    @abc.abstractmethod 
    def notifyChangeListeners():
        pass
    


    
