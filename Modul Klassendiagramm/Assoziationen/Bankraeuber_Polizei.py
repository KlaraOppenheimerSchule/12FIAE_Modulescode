class Polizei:
    def __init__(self, name):
        self.__name = name

    def patrouilliere(self):
        print(f"{self.__name} patrouilliert im Viertel.")

    def getName(self):
        return self.__name


class Bankraeuber:
    def __init__(self, name):
        self.__name = name
   

    def beobachtePolizei(self, polizei):
        print(f"Ich, {self.__name}, beobachte" f" {polizei.getName()}")
       


# Beispielhafte Nutzung
p = Polizei("Kommissarin Klarblick")
r = Bankraeuber("Räuber Ratz")

p.patrouilliere()
r.beobachtePolizei(p)

