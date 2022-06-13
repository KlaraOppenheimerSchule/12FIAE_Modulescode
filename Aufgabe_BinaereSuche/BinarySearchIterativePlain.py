from random import randint

class BinarySearchIterative():

    def runAlgorithm(self, list, seachedValue):
        iterations=0
        #
        # Implement code here
        #
        
        return iterations   
 

class Programm:
    def __init__(self, SearchAlgorithm, searchValue):
        self.__searchStrategy = SearchAlgorithm
        self.__searchValue=searchValue
        self.createList()

    def createList(self):
        self.__list=[randint(0,100) for i in range(60)]
        self.__list.sort()

    def runSearch(self):
        self.createList()
        return self.__searchStrategy.runAlgorithm(self.__list, self.__searchValue)



#Run binary search iterative
searchAlgorithm = BinarySearchIterative()
programm = Programm(searchAlgorithm, 42)
sumOfIterations=0

for i in range(1000):
    iteration=programm.runSearch()
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - binary search iterative:", round(avgIteration,1))

