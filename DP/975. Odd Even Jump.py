'''
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.
'''

class Solution:
    #method 1. DP. O(nlogn), S(n)
    def oddEvenJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        arr_index = [(a, i) for i, a in enumerate(arr)]
        arr_index.sort()
        next_higher = [0 for _ in range(len(arr))]
        next_lower = [0 for _ in range(len(arr))]
        
        stack = []
        #find next_higher indices for every element
        for i in range(len(arr)):
            _ , index = arr_index[i]
            while stack and stack[-1] < index:
                next_higher[stack.pop()] = index
            stack.append(index)
        
        # important!. Example: [(1, 0), (1, 1)] -> [(1, 1), (1, 0)] if just reverse the above arr_index.
        # Thus, sort (-a, i) instead and [(-1, 0), (-1, 1)] -> [(-1, 0), (-1, 1)]
        arr_index = [(-a, i) for i, a in enumerate(arr)]
        arr_index.sort()
        stack = []
        #find next_lower indices for every element
        for i in range(len(arr)):
            _ , index = arr_index[i]
            while stack and stack[-1] < index:
                next_lower[stack.pop()] = index
            stack.append(index)
            
        canVisit_odd = [0 for _ in range(len(arr))]
        canVisit_even = [0 for _ in range(len(arr))]
        canVisit_odd[-1] = 1
        canVisit_even[-1] = 1
        for i in range(len(arr) - 2, -1, -1):
            #An odd step: whether a position can finally reach the end 
            #is decided by its next high position
            canVisit_odd[i] = canVisit_even[next_higher[i]]
            #An even step: whether a position can finally reach the end 
            #is decided by its next low position            
            canVisit_even[i] = canVisit_odd[next_lower[i]]
        return sum(canVisit_odd)
        
        
