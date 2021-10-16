'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        n = len(nums)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if mid - 1 >= 0: num_left = nums[mid - 1]
            else: num_left = -inf
            
            if mid + 1 < n: num_right = nums[mid + 1]
            else: num_right = -inf
            
            if nums[mid] > num_left and nums[mid] > num_right: return mid
            elif nums[mid] < num_left and nums[mid] > num_right: right = mid
            elif nums[mid] > num_left and nums[mid] < num_right: left = mid
            else: right = mid
        
        if nums[left] > nums[right]: return left
        else: return right
