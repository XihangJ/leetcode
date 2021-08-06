'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution:
    #method 1. hashmap. O(n), S(n)
    from collections import Counter
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        res = []
        for num in nums2:
            if num in d1 and d1[num] > 0:
                res.append(num)
                d1[num] -= 1
        return res
