from stuhl import stuhl

class meister:
    def __init__(self):
        self.__laune = True
        self.__stuehle = []
       
    def setLaune(self,laune):
        self.__laune = laune
    
    def getLaune(self):
        return self.__laune
  
    def addStuhl(self, gebauterStuhl : stuhl):
        self.__stuehle.append(gebauterStuhl)
    
    def getStuhlQualitaet(self, index):
        return self.__stuehle[index].getQualitaet()
    
    def anwtortAufPauseGeben(self):
        antwort = "Wir gehen Eis essen!"
        return antwort
     
            
    def pruefeArbeit(self):
        
        length = len(self.__stuehle)
       
        for i in range (length):
            qualitaet = self.__stuehle[i].getQualitaet()
        
            if (qualitaet == True):
                print("Gute Arbeit")
            else:
                print("Mach es noch mal!")