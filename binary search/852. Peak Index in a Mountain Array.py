'''
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
'''

class Solution:
    #binary search
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]: return mid
            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]: left = mid
            else: right = mid
