import random
import time
#from algorithms.sorting import quick_sort as qs

sortedArray = []

size = 100000
unsortedArray = [0 for x in range(size)]

'''
Range of values to be stored
Negative values are at the 
end of the array in reverse order.

Next version should handle negative values
in a more traditional manner
'''
lowerBoundArrVal = 10 
upperBoundArrVal = 1000
#containsNegatives = False

#populating array, not relevant to runtime
for i in range(0, size):
    unsortedArray[i] = random.randint(lowerBoundArrVal, upperBoundArrVal)
random.shuffle(unsortedArray)
#print("Unsorted: ", unsortedArray)

'''
calculates the most significant bit
of the array by finding the max value and
shifting right
'''
def getMaxBit(size, arr = []):
    maxVal = 0
    maxBit = 0
    
    for i in range(0, size):
        if arr[i] > maxVal:
            maxVal = arr[i]
    
    while maxVal > 0:
        maxVal = maxVal>>1
        maxBit+=1
        
    return maxBit-1

'''
Uses bitwise operators to split arrays into top and bottom
lists. It then calls recursively on these lists to split them.
Continues until maxBit == 0, then adds to the sorted array in 
descending order.
'''
def bitSort(maxBit, size, arr = [], sortedArray = []):
    
    topArr = []
    botArr = []
    
    for x in arr:
        if(x & 2**maxBit == 2**maxBit): #ANDing with the current highest order bit
            topArr.append(x) #x at 2**maxBit is a 1
        else:
            botArr.append(x) #x at 2**maxBit is a 0
    
    if (maxBit > 0):
        #recursive case
        if(len(topArr)>0): #muh efficiencies
            bitSort(maxBit-1, size, topArr, sortedArray)
        if(len(botArr)>0):
            bitSort(maxBit-1, size, botArr, sortedArray)
    else:
        if(len(topArr) > 0):
            for i in range(len(topArr)): #handles duplicates
                    sortedArray.append(topArr[i])
        if(len(botArr) > 0):
            for i in range(len(botArr)):
                    sortedArray.append(botArr[i])    
    if(len(sortedArray) == size): #all elements are now in the array
        return sortedArray

bitSortStartTime = time.time()

maxBit = getMaxBit(size, unsortedArray)
sortedArray = bitSort(maxBit, size, unsortedArray, sortedArray)
sortedArray = sortedArray[::-1]
print("Sorted: ", sortedArray)
#print(len(sortedArray))

bitSortEndTime = time.time()
bitSortTotal = bitSortEndTime-bitSortStartTime
print("BitSort Time: ", bitSortTotal)

'''
#Uncomment for Qsort comparison
quickSortStartTime = time.time()
quickSortedArray = qs.sort(unsortedArray)
quickSortEndTime = time.time()
quickSortTotal = quickSortEndTime-quickSortStartTime
#print(quickSortedArray)
#print("QuickSort: ", quickSortTotal)
'''