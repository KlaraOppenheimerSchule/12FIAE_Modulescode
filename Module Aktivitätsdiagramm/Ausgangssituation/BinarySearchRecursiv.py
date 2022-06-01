from SearchAlgorithm import SearchAlgorithm
          
class BinarySearch(SearchAlgorithm):

    def __init__(self):
        self.__iteartions=0

    def resetIterationCounter(self):
        self.__iteartions=0

    def runAlgorithm(self, s, x):
        self.__iteartions=self.__iteartions+1
        #print("Iteration: ", self.__iteartions)
        #print(s)
        if len(s)==1:
            if s[0]==x:
                print("SearchValue found in iteration: ", self.__iteartions)
                return self.__iteartions           
            else:
                print("SearchValue not found")
                return self.__iteartions   
        
        else:
            m=s[len(s)//2]
            if x >=m:
                #TODO: Link zur Rekursionserklärung anfügen
                return self.runAlgorithm(s[len(s)//2:],x)
            else:
                return self.runAlgorithm(s[:len(s)//2],x)
                