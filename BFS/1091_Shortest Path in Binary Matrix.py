'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''

class Solution:
    # BFS. O(n ** 2), S(n)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], 
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]
        if grid[0][0] != 0 or grid[-1][-1] != 0: return -1
        if grid == [[0]]: return 1
        
        def bfs(row,col):
            count = 1
            queue = collections.deque([(row, col)])
            grid[row][col] = -1
            while queue:
                count += 1
                size = len(queue)
                for _ in range(size):
                    row, col = queue.popleft()
                    for direction in directions:
                        dr, dc = direction
                        r = row + dr
                        c = col + dc
                        if r == len(grid) - 1 and c == len(grid[0]) - 1: return count
                        if r >= 0  and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 0:
                            queue.append((r, c))
                            grid[r][c] = -1
            if grid[len(grid) - 1][len(grid[0]) - 1] == -1: return count
            else: return -1
        return bfs(0, 0)
