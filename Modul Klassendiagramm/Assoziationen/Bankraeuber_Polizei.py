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
       


''' Beispielhafte Nutzung
Hierbei ist die Kommunikation zumindest von einer Seite spezifiziert. Der Bankräuber kann sich den
Namen des Polizisten geben lassen. Dies bedeutet nicht, dass nicht (zukünftig) der Polizist den
Bankräuber kennt und sich den Namen geben lassen kann. Zumindest ist es aber jetzt nicht spezifiziert.
Ein Verbot besteht nicht.
'''
p = Polizei("Kommissarin Klarblick")
r = Bankraeuber("Räuber Ratz")

p.patrouilliere()
r.beobachtePolizei(p)

