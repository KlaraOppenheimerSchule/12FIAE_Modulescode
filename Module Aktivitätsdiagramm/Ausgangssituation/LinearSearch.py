from SearchAlgorithm import SearchAlgorithm

class LinearSearch(SearchAlgorithm):
    
    def runAlgorithm(self, list, searchValue):
        iterations=0
        for i in list:
            iterations=iterations+1
            if(i==searchValue):
                print("Found value. At listposition: ", iterations ,".In iteration:", iterations)
                return iterations
            
        print("Value not found")
        return iterations