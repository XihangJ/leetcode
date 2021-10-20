'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
'''

class Solution:
    # method 1. 2 pointers. O(m + n), S(1)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        res = []
        i1 = 0
        i2 = 0
        while i1 < len(firstList) and i2 < len(secondList):
            first = firstList[i1]
            second = secondList[i2]
            left, right = max(first[0], second[0]), min(first[1], second[1])
            
            if left <= right: res.append([left, right])
                
            if first[1] < second[1]: 
                i1 += 1
            elif first[1] > second[1]: 
                i2 += 1
            else: 
                i1 += 1
                i2 += 1
        return res
