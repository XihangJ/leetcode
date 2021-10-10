'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

class Solution:
    #method 1. BFS. O(mn), S(mn)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        fresh = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2: queue.append((row, col))
                if grid[row][col] == 1: fresh += 1
        if fresh == 0: return 0
        
        minute = -1
        while queue:
            minute += 1
            curr_len = len(queue)
            for _ in range(curr_len):
                row, col = queue.popleft()
                for direction in directions:
                    dr, dc = direction
                    r = row + dr
                    c = col + dc
                    if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1:
                        queue.append((r, c))
                        grid[r][c] = 2
                        fresh -= 1
        if fresh == 0: return minute
        else: return -1
            
