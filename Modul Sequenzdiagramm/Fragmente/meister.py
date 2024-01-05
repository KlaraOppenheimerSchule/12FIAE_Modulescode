from stuhl import stuhl

class meister:
    def __init__(self):
        self.__laune = True
        self.__stuehle = []
       
    def setLaune(self,laune):
        self.__laune = laune
    
    def getLaune(self):
        return self.__laune
  
    def setStuhl(self, gebauterStuhl : stuhl):
        self.__stuehle.append(gebauterStuhl)
    
    def getStuhlQualitaet(self, index):
        return self.__stuehle[index].getQualitaet()
    
    def anwtortAufPause(self):
        print("Wir gehen Eis essen!")
     
            
    def pruefeArbeit(self, index):
        
        qualitaet = self.__stuehle[index].getQualitaet()
        
        if (qualitaet == True):
            print("Gute Arbeit")
        else:
            print("Mach es noch mal!")