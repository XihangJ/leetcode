'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''

class Solution:

    #method 1. BFS. O(mn), S(mn)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        directions = ['>', '<', '^', 'v']
        layer = 0
        while queue:
            layer += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for direction in directions:
                    end = self.move(curr, m, n, direction)
                    if end not in visited:
                        visited.add(end)
                        queue.append(end)
                        mat[end[0]][end[1]] = layer
        return mat
        
        
    def move(self, curr, m, n, direction):
        dx, dy = 0, 0
        if direction == '>': dy = 1
        elif direction == '<': dy = -1
        elif direction == '^': dx = -1
        elif direction == 'v': dx = 1
        
        x, y = curr
        x += dx
        y += dy
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return curr
        else:
            return (x, y)
