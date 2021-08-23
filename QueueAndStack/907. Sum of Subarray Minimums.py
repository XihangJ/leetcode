'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
'''

class Solution:
    #method 2. stack. O(n), S(n)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 1: return arr[0]
        n = len(arr)        
        left_length = [0 for _ in range(n)]
        right_length = [0 for _ in range(n)]
        stack1, stack2 = [], []
        for i in range(n):
            if i == 0: 
                left_length[i] = 1
                stack1.append([i, 1])
            else:
                count = 0
                while stack1 and arr[i] < arr[stack1[-1][0]]: 
                    prev = stack1.pop()[1]
                    count += prev
                left_length[i] = 1 + count
                stack1.append([i, left_length[i]])
        
        for i in range(n - 1, -1, -1):
            if i == n - 1: 
                right_length[i] = 1
                stack2.append([i, 1])
            else:
                count = 0
                while stack2 and arr[i] <= arr[stack2[-1][0]]: 
                    prev = stack2.pop()[1]
                    count += prev
                right_length[i] = 1 + count
                stack2.append([i, right_length[i]])
        
        res = 0
        for i in range(n):
            res += arr[i] * (left_length[i] * right_length[i])
        return res % (10 ** 9 + 7)
    '''
    #method 1. DP. O(n ^ 2), S(n ^ 2). Time limit exceeded.
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 1: return arr[0]
        n = len(arr)
        mat = [[0 for _ in range(n)] for _ in range(n)]
        res = 0
        for length in range(1, n + 1):
            for row in range(n - length + 1):
                col = row + length - 1
                if row == col:
                    mat[row][col] = arr[row]
                else:
                    mat[row][col] = min(mat[row][col - 1], arr[col])
                res += mat[row][col]
        return int(res % (1e9 + 7))
    '''    
