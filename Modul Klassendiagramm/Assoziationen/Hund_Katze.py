
class Hund():
    def __init__(self, name):
        self.__name = name
    
    def __schnarchen(self):
        return "RRRRRCHHHHH"
    
    # Katze hat private Methode, daher so nicht möglich
    def bringeKatzeZumSchnurren(self, katze):
        katze.schnurren() # nicht möglich! Methode ist privat      

class Katze():
    def __init__(self, name):
        self.__name = name
        
    def __schnurren(self):
        return "Mrrrrrr"
    
    # Hund hat private Methode, daher so nicht möglich
    def bringeHundzumSchnarchen(self, hund):
        hund.schnarchen() # nicht möglich! Methode ist privat
    
''' Beipsielnutzung
 Das Verbot der Navigirbarkeit bringt zum Ausdruck, dass die Klassen nichts
voneindner wissen sollen. Dies kann z.B. so realisiert werden, dass Methoden
komplett auf privat gesetzt werden (erschwert dann auch die Kommunikation mit
anderen Klassen) oder man gestaltet die Methoden so aus, dass überprüft wird
welche Klasse Zugriff verlangt und man dies unterbindet. Generell ist der 
Hinweis auf Verbot eine klare Anweisung an den Entwickler, die Kommunikation
zwischen den betreffenden Klassen zu unterbinden / versagen.
'''
sassi = Katze("sassi")
balou = Hund("balou")

# geht nicht!
sassi.bringeHundzumSchnarchen(balou)
