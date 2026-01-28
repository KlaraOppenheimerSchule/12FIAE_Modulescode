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
    def __init__(self, strassenname, miete, spielername, konto):
        if not spielername or not konto:
            raise ValueError("Objekterstellung nicht erlaubt.")
            print("Objekt wird nicht erzeugt!")

        else:
            self.__strassenname = strassenname
            self.__miete = miete
            self.__besitzer = spieler(spielername,konto)
            print("Objekt wird erzeugt!")
    
    #getBesitzer
    def getBesitzer(self):
        return self.__besitzer.getName()
    


try:
    st1 = strasse('Badstrasse',1000.00, "Stefan",100)
    st2 = strasse('Badstrasse',1000.00, None, None)
except ValueError as e:
    print(e)
    
print(st1.getBesitzer())




