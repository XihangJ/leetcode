'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    
    #method 2. single for loop. O(min(m, n)), S(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n % 2 == 0:
                return (nums2[(n - 1) // 2] + nums2[n // 2]) / 2
            else:
                return float(nums2[n // 2])
        
        leftSize = (m + n) // 2
        for i in range(m + 1):
            j = m - i
            
            if i == 0:
                leftMax = nums2[leftSize - 1]
            elif leftSize == m and i == m:
                leftMax = nums1[i - 1]
            else:
                leftMax = max(nums1[i - 1], nums2[leftSize - i - 1])
            
            if j == 0:
                rightMin = nums2[leftSize - i]
            elif n == m and j == m:
                rightMin = nums1[0]
            else:
                rightMin = min(nums1[i], nums2[leftSize - i])
            
            if leftMax <= rightMin:
                if (m + n) % 2 == 0: return (leftMax + rightMin) / 2
                else: return float(rightMin) 
    
    
    '''
    #method 1. binary search -> median O(log(m + n)), S(m + n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        if not nums1:
            return (nums2[n // 2] + nums2[-1 - n // 2]) / 2
        
        if m == 1 and n == 1:
            return (nums1[0] + nums2[0]) / 2
        
        left, right = 0, m
        while left <= right and left >= 0 and right <= m:
            i = (left + right) // 2
            j = (m + n) // 2 - i
            if i == 0:
                if nums2[j - 1] <= nums1[0] and j < n:
                    if (m + n) % 2 != 0:
                        return min(nums1[0], nums2[j])
                    else:
                        return (min(nums1[0], nums2[j]) + nums2[j - 1]) / 2
                elif nums2[j - 1] <= nums1[0] and j == n: 
                    return (nums2[j-1] + nums1[0]) / 2
                else:
                    left = i + 1
                    print(left)
            elif j == 0:
                if nums1[i - 1] <= nums2[0]:
                    if (m + n) % 2 != 0:
                        return nums2[0]
                    else:
                        return (nums1[i - 1] + nums2[0]) / 2
                else:
                    right = i - 1
                    
            elif m - i == 0:
                if j == 0:
                    if (m + n) % 2 != 0:
                        return nums2[0]
                    else:
                        return (nums1[i - 1] + nums2[0]) / 2
                else:
                    if (m + n) % 2 != 0:
                        return nums2[j]
                    else:
                        return (max(nums1[i - 1], nums2[j - 1]) + nums2[j]) / 2
            
            elif nums1[i - 1] <= nums2[j] and nums2[j - 1] <= nums1[i]:
                if (m + n) % 2 != 0:
                    return min(nums1[i], nums2[j])
                else:
                    return (min(nums1[i], nums2[j]) + max(nums1[i-1], nums2[j-1])) / 2
            
            elif nums1[i - 1] > nums2[j]:
                right = i - 1
            elif nums2[j - 1] > nums1[i]:
                left = i + 1
    '''
