import abc
class Fahrzeug(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fahre():
        pass
    
class Auto(Fahrzeug):
    def fahre():
       print ("Brum Brum Brum")


class Motorrad(Fahrzeug):
    def fahre():
        print("Möp Möp Möp")


class FahrzeugFabrik(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def baue_Fahrzeug():
        pass
        

class AutoFabrik(FahrzeugFabrik):
    def baue_Fahrzeug():
        return Auto
             
class MotorradFabrik(FahrzeugFabrik):
    def baue_Fahrzeug():
        return Motorrad      

# Baue jetzt ein Auto
skoda = AutoFabrik.baue_Fahrzeug()
honda = MotorradFabrik.baue_Fahrzeug()

skoda.fahre()
honda.fahre()

