from stuhl import Stuhl
from meister import Meister
import random

class Lehrling:
    def __init__(self, meister: Meister):

        self.__meister = meister
        self.__fleissig = True

    def getFleissig(self):
        return self.__fleissig
    
    def setFleissig(self,fleissig):
        self.__fleissig = fleissig
    
    
    def frageNachPause(self):
        antwortmeister = self.__meister.anwtortAufPauseGeben()
        return antwortmeister
   
    def fegen(self):
        print("Feg, feg, feg ... ")
        
    def baueStuhl(self):
        status = bool(random.getrandbits(1))
        konkreterStuhl = Stuhl(status)
        self.__meister.addStuhl(konkreterStuhl)
    
    def baueStuehle(self, count):
        for i in range(count): 
            self.baueStuhl()
            
  
            
