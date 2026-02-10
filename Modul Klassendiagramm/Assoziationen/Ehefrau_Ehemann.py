
class Ehefrau():
    def __init__(self, vorname, kosename):
        self.__vorname = vorname
        self.__kosename = kosename
        self.__ehemann = None
    
    def getVorname(self):
        return self.__vorname

    def getKosename(self):
        return self.__kosename
    
    def setEhemann(self, ehemann):
        self.__ehemann = ehemann

    # hier die spezifische Navigierbarkeit
    def callEhemann(self):
        if self.__ehemann == None: 
            return None
        else:
            return self.__ehemann.getKosename()
    

class Ehemann():
    def __init__(self, vorname, kosename):
        self.__vorname = vorname
        self.__kosename = kosename
        self.__ehefrau = None
    
    def getVorname(self):
        return self.__vorname
    
    def getKosename(self):
        return self.__kosename
    
    def setEhefrau(self, ehefrau):
        self.__ehefrau = ehefrau

    # hier die spezifische Navigierbarkeit
    def callEhefrau(self):
        if self.__ehefrau == None: 
            return None
        else:
            return self.__ehefrau.getKosename()

''' Beispielhafte Nutzung
Hierbei ist die Navigierbarkeit spezifiziert (sie ist umgesetzt).
Und zwar in beide Richtungen (bidirektional).
Ehemann und Ehefrau werden als Objektreferenz aufgebaut und können über callEhemann / callEhefrau 
aufgerufen werden.
'''
andreas = Ehemann("Andreas","Schatz")
mona = Ehefrau("Mona","Hase")

andreas.setEhefrau(mona)
mona.setEhemann(andreas)

print(andreas.callEhefrau())
print(mona.callEhemann())