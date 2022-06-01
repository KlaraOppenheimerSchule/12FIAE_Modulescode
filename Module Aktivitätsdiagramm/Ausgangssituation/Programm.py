from random import randint
from BubbleSort import BubbleSort
from BinarySearchIterative import BinarySearchIterative
from BinarySearchRecursivly import BinarySearchRecursivly
from LinearSearch import LinearSearch

class Programm:
    def __init__(self, SearchAlgorithm, SortAlgorithm):
        self.__searchStrategy = SearchAlgorithm
        self.__sortStrategy = SortAlgorithm

    def setSearchAlgorithm(self, searchAlgorithm):
        self.__searchStrategy=searchAlgorithm

    def setSortAlgorithm(self, sortAlgorithm):
        self.__sortStrategy=sortAlgorithm

    def runSort(self, list):
        return self.__sortStrategy.runAlgorithm(list)

    def runSearch(self, list, searchValue):
        return self.__searchStrategy.runAlgorithm(list, searchValue)

    def resetConter(self):
             self.__searchStrategy.resetIterationCounter()


#Run lineare search
searchAlgorithm = LinearSearch()
sortAlgorithm = None
programm = Programm(searchAlgorithm, sortAlgorithm)
sumOfIterations=0

for i in range(1000):
    list=[randint(0,100) for i in range(60)]
    searchValue=42
    iteration=programm.runSearch(list, searchValue)
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - linear serch: ", avgIteration )


#Run binary search iterative
print("------------------")
searchAlgorithm = BinarySearchIterative()
sortAlgorithm = BubbleSort()

programm.setSearchAlgorithm(searchAlgorithm)
programm.setSortAlgorithm(sortAlgorithm)
sumOfIterations=0
for i in range(1000):
    list=[randint(0,100) for i in range(60)]
    searchValue=42
    programm.runSort(list)
    iteration=programm.runSearch(list, searchValue)
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - binary search iterative:", avgIteration)


#Run binary search recursively
print("------------------")
searchAlgorithm = BinarySearchRecursivly()
sortAlgorithm = BubbleSort()

programm.setSearchAlgorithm(searchAlgorithm)
programm.setSortAlgorithm(sortAlgorithm)
sumOfIterations=0
for i in range(1000):
    programm.resetConter()
    list=[randint(0,100) for i in range(60)]
    searchValue=42
    programm.runSort(list)
    iteration=programm.runSearch(list, searchValue)
    sumOfIterations=sumOfIterations+ iteration

avgIteration=sumOfIterations/1000
print("Average number of iterations - binary search recursivly:", avgIteration)