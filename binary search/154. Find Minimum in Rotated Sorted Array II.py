'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #1. Find the minimum position of nums
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            elif nums[mid] == nums[end]:
                end = end - 1 
        return min(nums[start], nums[end])
    
    
    
    '''
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]: return nums[0]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[left]: left = mid
            elif nums[mid] < nums[left]: right = mid
            elif nums[mid] == nums[left]: 
                if nums[left + 1] < nums[-1]: return nums[left + 1]
                left += 1
        return min(nums[left], nums[right])
    '''
