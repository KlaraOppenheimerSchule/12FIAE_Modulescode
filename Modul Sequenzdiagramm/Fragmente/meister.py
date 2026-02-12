from stuhl import Stuhl

class Meister:
    def __init__(self):
        self.__laune = True
        self.__stuehle = []
       
    def setLaune(self,laune):
        self.__laune = laune
    
    def getLaune(self):
        return self.__laune
  
    def addStuhl(self, gebauterStuhl : Stuhl):
        self.__stuehle.append(gebauterStuhl)
    
    def getStuhlQualitaet(self, index):
        return self.__stuehle[index].getQualitaet()
    
    def anwtortAufPauseGeben(self):
        antwort = "Wir gehen Eis essen!"
        return antwort
     
            
    def pruefeArbeit(self, index):
        
        qualitaet = self.__stuehle[index].getQualitaet()
        
        if (qualitaet == True):
            print("Gute Arbeit")
        else:
            print("Mach es noch mal!")