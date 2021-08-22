'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''

class Solution:
    #method 1. BFS with a visited set. O(N), S(N)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1: return -1
        elif n == 1: return 1
        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        directions = ['>', '<', '^', 'v', '>v', '>^', '<v', '<^']
        count = 1
        while queue:
            count += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for direction in directions:
                    end = self.move(curr, n, direction)
                    if end == (n - 1, n - 1) and grid[end[0]][end[1]] == 0: return count
                    elif end not in visited and grid[end[0]][end[1]] == 0:
                        visited.add(end)
                        queue.append(end)
        return -1
            
            
    def move(self, curr, n, direction):
        dx, dy = 0, 0
        if '>' in direction: dy = 1
        if '<' in direction: dy = -1
        if '^' in direction: dx = -1
        if 'v' in direction: dx = 1
        
        x, y = curr
        x += dx
        y += dy
        
        if x < 0 or x >= n or y < 0 or y >= n:
            return curr
        else:
            return (x, y)
