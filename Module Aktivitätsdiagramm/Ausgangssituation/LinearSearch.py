from SearchAlgorithm import SearchAlgorithm

class LinearSearch(SearchAlgorithm):
    
    def runAlgorithm(self, list, searchValue):
        iterations=0

        for i in list:
            if(i==searchValue):
                print("Found value. At listposition: ", iterations ,".In iteration:", iterations)
                return iterations
                
            iterations=iterations+1

        #print("Value not found")
        return iterations