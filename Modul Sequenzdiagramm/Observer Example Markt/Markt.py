import abc

# Abstrakte Klasse Markt
class Markt(metaclass=abc.ABCMeta):

    def __init__(self,name):
        self.__name = name
        self.__observer = []
        self.__angebot=""
        self.__message ="Angebote sind da!"
    
    def getName(self):
        return self.__name

    def addObserver(self,observer):
        self.__observer.append(observer)
    
    def getAngebot(self):
        return self.__angebot
    
    def getMessage(self):
        return self.__message


    def setAngebot(self,angebot):
        self.__angebot = angebot
        self.notifyObserver()

    def notifyObserver(self):
        for x in self.__observer:
            x.update(self)
