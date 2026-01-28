from pickle import FALSE, NONE

class spieler():
       
    
#constructor
    def __init__(self, spielername, konto):
        self.__spielername = spielername
        self.__konto = konto
        
#getName
    def getName(self):
        return self.__spielername
  
# Class Strasse
class strasse():
     
    #constructor
    def __init__(self, strassenname, miete):
        self.__strassenname = strassenname
        self.__miete = miete
        self.__besitzer = [spieler] = NONE
    
    #getBesitzer
    def getBesitzer(self):
        if self.__besitzer is NONE:
            return 'Die Strasse hat keinen Besitzer'
        else:
            return self.__besitzer.getName()
    
    
    #addBesitzer
    def addBesitzer(self, besitzer):
        self.__besitzer = besitzer
        
      
    #Remove Besitzer      
    def removeBesitzer(self):
        self.__besitzer = NONE

# Test   
sp1 = spieler('Stefan', 100.00)
st1 = strasse('Badstrasse',1000.00)

# Besitzer hinzufügen
##st1.addBesitzer(sp1)

# Besitzer ausgeben lassen
#print(st1.getBesitzer())

# Besitzer entfernen
#st1.removeBesitzer()

# Besitzer ausgeben lassen
#print(st1.getBesitzer())

print(sp1.getName())
