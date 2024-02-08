from ChangeListener import ChangeListener
from FilmDaten import FilmDaten

class AnzeigeBeliebt(ChangeListener):
    def __init__(self, Filmdaten : FilmDaten):
        self.__Filmdaten = Filmdaten
        self.__beliebt = []
        self.__tipp = []
        
    def display(self):
        print ("Beliebte Filme:",self.__beliebt,"\n Filmtipp:",self.__tipp)
        

    def update(self):
        self.__beliebt = self.__Filmdaten.getBeliebt()
        self.__tipp = self.__Filmdaten.getTipp()
        self.display()
       