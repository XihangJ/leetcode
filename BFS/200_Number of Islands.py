'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        #method 2. BFS O(m*n), S(min(m,n))
        from collections import deque
        queue = deque()
        count = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    count += 1
                    grid[row][col] = '0'
                    queue.append((row, col))
                    while queue:
                        i, j = queue.popleft()
                        #print(i, j)
                        if i - 1 >= 0 and j >= 0 and i - 1 < m and j < n:
                            if grid[i - 1][j] == '1':
                                queue.append((i - 1, j))
                                grid[i - 1][j] = '0'
                        if i + 1 >= 0 and j >= 0 and i + 1 < m and j < n:
                            if grid[i + 1][j] == '1':
                                queue.append((i + 1, j))
                                grid[i + 1][j] = '0'
                        if i >= 0 and j - 1 >= 0 and i < m and j - 1 < n:
                            if grid[i][j - 1] == '1':
                                queue.append((i, j - 1))
                                grid[i][j - 1] = '0'
                        if i >= 0 and j + 1 >= 0 and i < m and j + 1 < n:
                            if grid[i][j + 1] == '1':
                                queue.append((i, j + 1))
                                grid[i][j + 1] = '0'
        return count    
    '''
        #method 1. DFS O(m*n), S(m*n)
        count = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        return count
                
    def dfs(self, grid, row, col):
        m = len(grid)
        n = len(grid[0])
        if row >= m or col >= n or grid[row][col] != '1' or row < 0 or col < 0:
            return
        grid[row][col] = '0'
        self.dfs(grid, row + 1, col + 0)
        self.dfs(grid, row - 1, col + 0)
        self.dfs(grid, row + 0, col - 1)
        self.dfs(grid, row + 0, col + 1)
    '''
