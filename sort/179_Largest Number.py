'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

#method 1. Build in sort. Build a comparator.
#O(nlogn), S(logn) or S(n)

class Comparator(str):
    def __lt__(x, y):
        return x + y < y + x
    def __gt__(x, y):
        return x + y > y + x
    def __eq__(x, y):
        return x + y == y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1: return str(nums[0])
        nums.sort(reverse = True, key = Comparator)
        if nums[0] == 0:
            return '0'
        else:
            res = ''.join(str(num) for num in nums)
        return res
