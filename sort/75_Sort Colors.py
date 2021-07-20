'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

class Solution:
    #method 1. 2 partitions. O(n), S(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        
        # 1st partition. Put 0s in the left part of nums
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < 1:
                left += 1
            while left <= right and nums[right] >= 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 2st partition. Put 2s in the right part of nums
        if left - right != 1:
            left = right + 1
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == 1:
                left += 1
            while left <= right and nums[right] == 2:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return
