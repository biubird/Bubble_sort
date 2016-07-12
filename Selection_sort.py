import random
import time
startTime = time.time()

myList = random.sample(xrange(10000), 100)
print myList

def Selection_sort(myList):
    for i in range(len(myList)):
        MaxPosition = i
        for location in range(i+1, len(myList) ):
            if myList[location]>myList[MaxPosition]:
                MaxPosition = location

def swap_indices(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp

    return myList
    
elapsedTime = time.time() - startTime
print elapsedTime
