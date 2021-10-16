'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    #method : Binary Search. O(logn), S(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        n = len(nums)
        
        # 1. find the starting position of a given target
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if nums[left] == target: first = left
        elif nums[right] == target: first = right
        else: first = -1
        if first == -1: return [-1, -1]  
        
        # 2. find the last position of a given target
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if nums[right] == target: last = right
        elif nums[left] == target: last = left
        else: last = -1
            
        return [first, last]
