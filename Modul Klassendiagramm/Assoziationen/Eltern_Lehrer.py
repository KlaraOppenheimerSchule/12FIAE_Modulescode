class Eltern:
    def __init__(self, name):
        self.__name = name
        self.__interesse = True

    def getElternname(self):
        return self.__name

    def anrufen(self):
        print(f"{self.__name} wird angerufen.")


class Lehrer:
    def __init__(self, name):
        self.__name = name
        self.__interesse = True

    def getLehrername(self):
        return self.__name

    def anrufen(self):
        print(f"{self.__name} wird angerufen.")

''' Beispiel der Nutzung:
Aufgrund der unspezifischen Navigierbarkeit rufen weder Klasse Lehrer noch Klasse Eltern 
Methoden der anderen Klasse auf. Bei der unspezifischen Navigierbarkeit ist dies jedoch 
noch verboten, aber auch nicht explizit gefordert. Es ist halt nicht spzeifiziert (unspezifisch)
'''
lehrer1 = Lehrer("Herr Weber")
eltern1 = Eltern("Frau Schulz")


