from random import randint
from BinarySearchIterative import BinarySearchIterative
from BinarySearchRecursivly import BinarySearchRecursivly
from LinearSearch import LinearSearch

class Programm:
    def __init__(self, SearchAlgorithm, searchValue):
        self.__searchStrategy = SearchAlgorithm
        self.__searchValue=searchValue
        self.createList()

    def createList(self):
        self.__list=[randint(0,100) for i in range(60)]
        self.__list.sort()

    def setSearchAlgorithm(self, searchAlgorithm):
        self.createList()
        self.__searchStrategy=searchAlgorithm

    def runSearch(self):
        return self.__searchStrategy.runAlgorithm(self.__list, self.__searchValue)

    def resetConter(self):
             self.__searchStrategy.resetIterationCounter()


#Run lineare search
searchAlgorithm = LinearSearch()
programm = Programm(searchAlgorithm, 42)
sumOfIterations=0

for i in range(1000):
    iteration=programm.runSearch()
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - linear search: ", round(avgIteration,1) )



#Run binary search iterative
print("------------------")
searchAlgorithm = BinarySearchIterative()
programm.setSearchAlgorithm(searchAlgorithm)
sumOfIterations=0

for i in range(1000):
    iteration=programm.runSearch()
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - binary search iterative:", round(avgIteration,1))



#Run binary search recursively
print("------------------")
searchAlgorithm = BinarySearchRecursivly()
programm.setSearchAlgorithm(searchAlgorithm)
sumOfIterations=0

for i in range(1000):
    programm.resetConter()
    iteration=programm.runSearch()
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - binary search recursivly:", round(avgIteration,1))
