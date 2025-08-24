
class Hund():
    def __init__(self, name):
        self.__name = name
    
    def __schnarchen(self):
        return "RRRRRCHHHHH"
    
    def bringeKatzeZumSchnurren(self, katze):
        katze.schnurren() # nicht möglich! Methode ist privat      

class Katze():
    def __init__(self, name):
        self.__name = name
        
    def __schnurren(self):
        return "Mrrrrrr"
    
    def bringeHundzumSchnarchen(self, hund):
        hund.schnarchen() # nicht möglich! Methode ist privat
    

# Beipsielnutzung

sassi = Katze("sassi")
balou = Hund("balou")
sassi.bringeHundzumSchnarchen(balou)
