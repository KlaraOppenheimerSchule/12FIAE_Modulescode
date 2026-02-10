
class Auktionator:
    def __init__(self):
        self.__gebot = ["", 0]  # [Name, Betrag]

    def setzeMaxGebot(self, name, betrag):
        if betrag > self.__gebot[1]:
            self.__gebot = [name, betrag]

    def getGebot(self):
        return self.__gebot


class Telefonbieter:
    def __init__(self, name, auktionator):
        self.__name = name
        self.__auktionator = auktionator

    def biete(self, betrag):
        self.__auktionator.setzeMaxGebot(self.__name, betrag)


''' Beispielhafte Nutzung
Hierbei ist die Kommunikation wie eine Einbahnstraße zu sehen. Der Auktionator schafft die 
Rahmen für die Versteigunger (Attribut gebote als Liste). Die Bieter haben stets Zugriff und
können bieten. Jedoch hat der Auktionator beim Verfahren keine Kenntnisse über die Bieter, da 
ihm laut Klassendiagramm eine Kommunikation in diese Richtung verboten wurde.
'''

a = Auktionator()
bieter1 = Telefonbieter("Bieter1",a)
bieter2 = Telefonbieter("Bieter2",a)
bieter3 = Telefonbieter("Bieter3",a)


bieter1.biete(20)
print(a.getGebot())  # ['Bieter1', 20]
bieter2.biete(40)
print(a.getGebot())  # ['Bieter2', 40]
bieter3.biete(35)
print(a.getGebot())  # ['Bieter2', 40]
