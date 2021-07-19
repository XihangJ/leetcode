def sortIntegers(A):
    if (A == [] or len(A) == 0):
        return
    quickSort(A, 0, len(A) - 1)


def quickSort(A, startIndex, endIndex):
    
    if (startIndex >= endIndex):
        return
    
    leftIndex = startIndex
    rightIndex =endIndex
    pivot = A[startIndex + (endIndex - startIndex) // 2]
    while (leftIndex <= rightIndex):
        while(leftIndex <= rightIndex and A[leftIndex] > pivot):
            leftIndex += 1
        while(leftIndex <= rightIndex and A[rightIndex] < pivot):
            rightIndex -= 1
        if (leftIndex <= rightIndex):
            temp = A[leftIndex]
            A[leftIndex] = A[rightIndex]
            A[rightIndex] = temp
            leftIndex += 1
            rightIndex -= 1
    quickSort(A, startIndex, rightIndex)
    quickSort(A, leftIndex, endIndex)
    return
