
class Auktionator:
    def __init__(self):
        self.__gebot = ["", 0]  # [Name, Betrag]

    def setzeMaxGebot(self, name, betrag):
        if betrag > self.__gebot[1]:
            self.__gebot = [name, betrag]

    def getGebot(self):
        return self.__gebot


class Telefonbieter:
    def __init__(self, name):
        self.__name = name

    def biete(self, auktionator, betrag):
        auktionator.setzeMaxGebot(self.__name, betrag)


''' Beispielhafte Nutzung
Hierbei ist die Kommunikation wie eine Einbahnstraße zu sehen. Der Auktionator schafft die 
Rahmen für die Versteigunger (Attribut gebote als Liste). Die Bieter haben stets Zugriff und
können bieten. Jedoch hat der Auktionator beim Verfahren keine Kenntnisse über die Bieter, da 
ihm laut Klassendiagramm eine Kommunikation in diese Richtung verboten wurde.
'''
bieter1 = Telefonbieter("Bieter1")
bieter2 = Telefonbieter("Bieter2")
bieter3 = Telefonbieter("Bieter3")
a = Auktionator()

bieter1.biete(a, 20)
print(a.getGebot())  # ['Bieter1', 20]
bieter2.biete(a, 40)
print(a.getGebot())  # ['Bieter2', 40]
bieter3.biete(a, 35)
print(a.getGebot())  # ['Bieter2', 40]
