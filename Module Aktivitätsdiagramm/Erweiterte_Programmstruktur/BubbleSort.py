from SortAlgorithm import SortAlgorithm

class BubbleSort(SortAlgorithm):
    def runAlgorithm(self, array):
        arrayLastIndex = len(array) - 1
        
        while arrayLastIndex > 0:
            for i in range(0, arrayLastIndex):
                if array[i] > array[i+1]:
                    array[i+1], array[i] = array[i],array[i+1]
            arrayLastIndex -=1
          
   