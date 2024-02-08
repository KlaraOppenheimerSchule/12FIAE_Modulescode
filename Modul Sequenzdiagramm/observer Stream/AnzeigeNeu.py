from ChangeListener import ChangeListener
from FilmDaten import FilmDaten

class AnzeigeNeu(ChangeListener):
    def __init__(self, Filmdaten : FilmDaten):
        self.__Filmdaten = Filmdaten
        self.__neu = []
        self.__beliebt = []
        self.__tipp = []
        
    def display(self):
        print(self.__neu,self.__beliebt,self.__tipp)
        

    def update(self):
        self.__neu.append(self.__Filmdaten.getNeu())
        self.__tipp.append(self.__Filmdaten.getTipp())
        self.__beliebt.append(self.__Filmdaten.getBeliebt())
        self.display()
    
    
class AnzeigeSchule (ChangeListener):
    def update(self):
        pass
