from SearchAlgorithm import SearchAlgorithm
          
class BinarySearchRecursivly(SearchAlgorithm):

    def __init__(self):
        self.__iteartions=0

    def resetIterationCounter(self):
        self.__iteartions=0

    def runAlgorithm(self, list, searchedValue):
        self.__iteartions=self.__iteartions+1
        #print("Iteration: ", self.__iteartions)
        #print(s)
        if len(list)==1:
            if list[0]==searchedValue:
                #print("SearchValue found in iteration: ", self.__iteartions)
                return self.__iteartions           
            else:
                #print("SearchValue not found")
                return self.__iteartions   
        
        else:
            m=list[len(list)//2]
            if searchedValue >=m:
                return self.runAlgorithm(list[len(list)//2:],searchedValue)
            else:
                return self.runAlgorithm(list[:len(list)//2],searchedValue)
                