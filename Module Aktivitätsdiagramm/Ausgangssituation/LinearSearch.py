from pickle import TRUE
from subprocess import list2cmdline
from SearchAlgorithm import SearchAlgorithm

class LinearSearch(SearchAlgorithm):
    
    def runAlgorithm(self, list, searchValue):
        iterations=0
        for i in list:
            iterations=iterations+1
            if(i==searchValue):
                print("Found value, in Iteration:", iterations)
                return True
        print("Value not found")
        return iterations