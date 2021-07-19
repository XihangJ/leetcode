'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #method 1. Sort first. O(nlogn) + O(n) = O(nlogn), S(n)
        if (len(intervals) == 1):
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            tmp = res[-1]
            if tmp[1] >= intervals[i][0] and tmp[1] < intervals[i][1]:
                tmp[1] = intervals[i][1]
            elif tmp[1] < intervals[i][0]:
                res.append(intervals[i])
        return res
