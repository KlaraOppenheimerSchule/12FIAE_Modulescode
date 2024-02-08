from SearchAlgorithm import SearchAlgorithm
          
class BinarySearchIterative(SearchAlgorithm):

    def runAlgorithm(self, list, seachedValue):
        iterations=0
        low = 0
        high = len(list) - 1
        mid = 0
 
        while low <= high:
            iterations=iterations+1
 
            mid = (high + low) // 2
 
            # If x is greater, ignore left half
            if list[mid] < seachedValue:
               low = mid + 1
 
            # If x is smaller, ignore right half
            elif list[mid] > seachedValue:
                high = mid - 1
 
            # means x is present at mid
            else:
                return iterations
 
        # If we reach here, then the element was not present
        #print("SearchValue not found")
        return iterations   
 
                