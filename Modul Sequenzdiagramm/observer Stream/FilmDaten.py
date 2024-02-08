from ObservedSubject import ObservedSubject

class FilmDaten (ObservedSubject):
    def __init__(self):
        self.__ChangeListener = []
        self.__neu = []
        self.__tipp = []
        self.__beliebt = []

    def addChangeListener(self, Changelistener):
        if Changelistener not in self.__ChangeListener:
            self.__ChangeListener.append(Changelistener)

    def removeChangeListener(self, ChangeListener):
        try:
            self.__ChangeListener.remove(ChangeListener)
        except ValueError:
            pass

    def set_data(self, neu, beliebt, tipp):
        self.__neu.append(neu)
        self.__beliebt.append(beliebt)
        self.__tipp.append(tipp)
        self.notifyChangeListeners()

    def notifyChangeListeners(self):
        for ChangeListener in self.__ChangeListener:
            ChangeListener.update()
    
    def getNeu(self):
        return self.__neu
    
    def getTipp(self):
        return self.__tipp
    
    def getBeliebt(self):
        return self.__beliebt







