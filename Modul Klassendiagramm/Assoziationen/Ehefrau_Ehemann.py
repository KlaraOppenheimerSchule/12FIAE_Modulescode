
class Ehefrau():
    def __init__(self, vorname, geburtsdatum, kosename):
        self.__vorname = vorname
        self.__kosename = kosename
    
    def getVorname(self):
        return self.__vorname

    def getKosename(self):
        return self.__kosename
    
    # hier die spezifische Navigierbarkeit
    def callEhemann(self, ehemann):
        return ehemann.getKosename()
    

class Ehemann():
    def __init__(self, vorname, kosename):
        self.__vorname = vorname
        self.__kosename = kosename
    
    def getVorname(self):
        return self.__vorname
    
    def getKosename(self):
        return self.__kosename
    
    # hier die spezifische Navigierbarkeit
    def callEhefrau(self, ehefrau): 
        return ehefrau.getKosename()

''' Beispielhafte Nutzung
Hierbei ist die Navigierbarkeit spezifiziert (sie ist umgesetzt).
Un zwar in beide Richtungen (bidirektional).
Um den Ehemann bzw. die Ehefrau anzrufen, ist im Code bei der
Methode callEhefrau / callEhemann die Übergabe der Klasse ehefrau bzw. 
ehemann erforderlich.
'''
ehemann1 = Ehemann("Andreas","09.05.1992","Schatz")
ehefrau1 = Ehefrau("Mona","09.04.1991","Hase")

print(ehemann1.callEhefrau(ehefrau1))
print(ehefrau1.callEhemann(ehemann1))