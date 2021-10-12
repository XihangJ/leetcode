'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''

class Solution:
    #method: DP. O(n ** 2), S(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col]
                elif col == len(triangle[row]) - 1:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col - 1]
                else:
                    triangle[row][col] = min(triangle[row - 1][col - 1], triangle[row - 1][col]) + triangle[row][col]
        return min(triangle[-1])
