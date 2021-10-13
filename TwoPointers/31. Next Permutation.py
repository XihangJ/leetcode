'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
'''

class Solution:
    #method 1. 2 pointers. O(n), S(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return nums
        n = len(nums)
        left, right = n - 2, n - 1
        need_reverse = True
        while left >= 0:
            if nums[left] < nums[right]:
                start = left
                need_reverse = False
                break
            left -= 1
            right -= 1
        
        if need_reverse: 
            nums.reverse()
            return nums
        
        # get the element's index that is the min of 
        #numbers that greater than nums[start]
        upper = inf
        for i in range(start + 1, n):
            if nums[i] > nums[start] and nums[i] <= upper: # take care!!! nums[i] <= upper to guarentee nums after start are in descending order
                exchange_index = i
                upper = nums[i]
        nums[start], nums[exchange_index] = nums[exchange_index], nums[start]
        # set nums after start in ascending order
        left, right = start + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        return nums
