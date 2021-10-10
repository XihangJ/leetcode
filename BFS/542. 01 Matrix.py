'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''

class Solution:
    
    #method 2. DP. O(mn), S(1)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #2 pass scan.
        if not mat: return
        m, n = len(mat), len(mat[0])
        #first: top left to bot right
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0: continue
                #top:
                r_top = row - 1
                if r_top >= 0 and r_top < m: max_top = mat[r_top][col]
                else: max_top = inf
                #left:
                c_left = col - 1
                if c_left >= 0 and c_left < n: max_left = mat[row][c_left]
                else: max_left = inf
                mat[row][col] = min(max_left + 1, max_top + 1)

        #second: bot right to top left
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if mat[row][col] == 0: continue
                #bot:
                r_bot = row + 1
                if r_bot >= 0 and r_bot < m: max_bot = mat[r_bot][col]
                else: max_bot = inf
                #right:
                c_right = col + 1
                if c_right >= 0 and c_right < n: max_right = mat[row][c_right]
                else: max_right = inf
                mat[row][col] = min(max_right + 1, max_bot + 1, mat[row][col]) # important! avoid marking inf in a cell
                
        return mat
        
    
    """
    #method 1. BFS. O(mn), S(mn)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = collections.deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1 #mark as unvisited
        while queue:
            row, col = queue.popleft()
            for direction in directions:
                dr, dc = direction
                r = row + dr
                c = col + dc
                if r >= 0 and r < len(mat) and c >= 0 and c < len(mat[0]) and mat[r][c] == -1:
                    mat[r][c] = mat[row][col] + 1
                    queue.append((r, c))
        return mat
    """
