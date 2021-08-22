'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
'''

class Solution:
    #method 1. BFS. O(mnk), S(mnk)
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1 and grid[0][0] == 0: return 0
        
        queue = collections.deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        
        while queue:
            row, col, k, steps = queue.popleft()
            for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if new_row >= 0 and new_row <= m - 1 and new_col >= 0 and new_col <= n - 1:
                    if grid[new_row][new_col] == 0 and (new_row, new_col) == (m - 1, n -1):
                        return steps + 1
                    elif grid[new_row][new_col] == 0 and (new_row, new_col, k) not in visited:
                        visited.add((new_row, new_col, k))
                        queue.append((new_row, new_col, k, steps + 1))
                    elif grid[new_row][new_col] == 1 and k > 0 and (new_row, new_col, k - 1) not in visited:
                        visited.add((new_row, new_col, k - 1))
                        queue.append((new_row, new_col, k - 1, steps + 1))
        return -1
