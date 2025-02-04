from Observer import *


class Exklusivkunde(Observer):
    def __init__(self,name):
        super().__init__(name)
    
    def update(self,markt):
        self.display(markt)
    
    def display(self,markt):
        print(markt.getName(),"meldet an Exklusivkunde",super().getName(),":",markt.getMessage())
    
