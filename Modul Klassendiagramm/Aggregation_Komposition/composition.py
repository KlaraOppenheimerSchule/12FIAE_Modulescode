from pickle import FALSE, NONE

# Class Strasse
class Strasse():
     
    #constructor
    def __init__(self, strassenname, miete):
        self.__strassenname = strassenname
        self.__miete = miete
    
    #get strassenname

    def getStrassenname(self):
        return self.__strassenname
    
    # get miete

    def getMiete(self):
        return self.__miete


# Class Spieler
class Spieler():
       

    #constructor
    def __init__(self, spielername : str, konto : float):
        self.__spielername = spielername
        self.__konto = konto
        self.__strasse = []
        
    #getName
    def getName(self):
        return self.__spielername
    
    #getKonto
    def getKonto(self):
        return self.__konto
    
    #get streetname by ID
    def getStrassennameByID(self, id : int):
        if 0 <= id < len(self.__strasse):
            return self.__strasse[id].getStrassenname()
        else:
            return None

    
    #increase the account balance
    def erhoeheKontostand(self, betrag : float):
        self.__konto += betrag

    # decrease the account balance

    def senkeKontostand(self, betrag : float):
        self.__konto -= betrag

    
    # add street to list
    def addStrasse(self, strassenname : str, miete : float):
        self.__strasse.append(Strasse(strassenname,miete))

    # remove street frome list
    def enterferneStrasseByID(self, index : int):
        self.__strasse.pop(index)
    


# Test   
player1 = Spieler("Stefan",100.00)

player1.addStrasse("Schlossalle",8000.00)

print(player1.getStrassennameByID(0))


player1.enterferneStrasse(0)

print(player1.getStrassennameByID(0))


