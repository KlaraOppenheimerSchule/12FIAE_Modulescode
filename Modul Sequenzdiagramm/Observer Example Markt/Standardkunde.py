from Observer import *

# Klasse Kunde implementiert Observer - update
class Standardkunde(Observer):
    def __init__(self,name):
        super().__init__(name)

    def update(self,markt):
        self.display(markt)
    
    def display(self,markt):
        print(markt.getName(),"meldet an",super().getName(),":",markt.getMessage())
