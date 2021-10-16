'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return -1
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: start = mid
            else: end = mid
        
        if matrix[start // n][start % n] == target: return True
        if matrix[end // n][end % n] == target: return True
        return False
