import abc
class Form(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def berechne_flaeche(self):
        pass

    @abc.abstractmethod
    def berechne_umfang(self):
        pass
    
class Rechteck(Form):
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def berechne_flaeche(self):
        return self.laenge * self.breite 

    def berechne_umfang(self):
        return 2 * (self.laenge + self.breite) 

class Quadrat(Form):
    def __init__(self, breite):
        self.breite = breite

    def berechne_flaeche(self):
        return self.breite ** 2

    def berechne_umfang(self):
        return 4 * self.breite

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius

    def berechne_flaeche(self):
        return 3.14 * self.radius * self.radius

    def berechne_umfang(self):
        return 2 * 3.14 * self.radius

class FormFabrik:
    def baue_Form(self, name):
        if name == 'Kreis':
            radius = input("Geben Sie den Radius des Kreises ein: ")
            return Kreis(float(radius))

        elif name == 'Rechteck':
            laenge = input("Geben Sie die Laenge des Rechtecks ein: ")
            breite = input("Geben Sie die Breite des Rechtecks ein: ")
            return Rechteck(int(laenge), int(breite))

        elif name == 'Quadrat':
            breite = input("Geben Sie die Breite des Quadrats ein: ")
            return Quadrat(int(breite))

def Form_Client():
    Form_Fabrik = FormFabrik()
    Form_Name = input("Geben Sie den Namen der Form ein: ")

    form = Form_Fabrik.baue_Form(Form_Name)

   
    print("Die Flaeche des",Form_Name," ist:",form.berechne_flaeche())
    print("Der Umfang des",Form_Name," ist:",form.berechne_umfang())
    


Form_Client()