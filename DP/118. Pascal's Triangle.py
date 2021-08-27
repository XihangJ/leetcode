'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        res = [[1], [1,1]]
        prev = [1, 1]
        nums = [1, 1]
        for row in range(2, numRows):
            nums.append(1)
            for i in range(1, row):
                nums[i] = prev[i - 1] + prev[i]
            prev = nums.copy()
            res.append(prev)
        return res
