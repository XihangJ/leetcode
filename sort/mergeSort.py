def sortIntegers(A):
    if (A == [] or len(A) == 0):
        return
    mergeSort(A, 0, len(A) - 1)

def mergeSort(A, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    midIndex = (startIndex + endIndex) // 2
    mergeSort(A, startIndex, midIndex)
    mergeSort(A, midIndex + 1, endIndex)
    merge(A, startIndex, endIndex)
    
def merge(A, startIndex, endIndex):
    temp=[]
    midIndex = (startIndex + endIndex) // 2
    leftIndex = startIndex
    rightIndex = midIndex + 1
    #select smaller element to fill in temp list
    while (leftIndex <= midIndex and rightIndex <= endIndex):
        if (A[leftIndex] > A[rightIndex]):
            temp.append(A[rightIndex])
            rightIndex += 1
        elif (A[leftIndex] < A[rightIndex]):
            temp.append(A[leftIndex])
            leftIndex += 1
    #check if there is any element left:
    while (leftIndex <= midIndex):
        temp.append(A[leftIndex])
        leftIndex += 1
    while (rightIndex <= endIndex):
        temp.append(A[rightIndex])
        rightIndex += 1
    for index in range(startIndex, endIndex + 1):
        A[index] = temp[index - startIndex]
