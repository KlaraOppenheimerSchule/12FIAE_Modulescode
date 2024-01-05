from stuhl import stuhl
from meister import meister
import random

class lehrling:
    def __init__(self, meister):

        self.__meister = meister
        self.__fleissig = True

    def getFleissig(self):
        return self.__fleissig
    
    def setFleissig(self,fleissig):
        self.__fleissig = fleissig
    
    
    def frageNachPause(self):
        self.__meister.anwtortAufPause()
   
    def fegen(self):
        print("Feg, feg, feg ... ")
        
    def baueStuhl(self):
        status = bool(random.getrandbits(1))
        konkreterStuhl = stuhl(status)
        self.__meister.setStuhl(konkreterStuhl)
    
    def baueStuehle(self, count):
        for i in range(count): 
            self.baueStuhl()
            
  
            
