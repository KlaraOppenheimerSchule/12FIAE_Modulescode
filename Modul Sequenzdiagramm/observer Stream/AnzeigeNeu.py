from ChangeListener import ChangeListener
from FilmDaten import FilmDaten

class AnzeigeNeu(ChangeListener):
    def __init__(self, Filmdaten : FilmDaten):
        self.__Filmdaten = Filmdaten
        self.__neu = []
        self.__tipp = []
        Filmdaten.addChangeListener(self)
        
    def display(self):
        print ("Neue Filme:",self.__neu,"\n Filmtipp:",self.__tipp)
        

    def update(self):
        self.__neu = self.__Filmdaten.getNeu()
        self.__tipp = self.__Filmdaten.getTipp()
        self.display()
    
    