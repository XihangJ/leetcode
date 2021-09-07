'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

class Solution:
    #method 1. BFS. O(n^2), S(n^2)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    break
            if grid[x][y] == 1:
                break
        queue.append((x, y))
        visited.add((x, y))
        count = 0
        while queue:
            x, y = queue.popleft()
            count += self.decideType(grid, x, y)
            for direction in directions:
                dx, dy = direction
                curr_x = x + dx
                curr_y = y + dy
                if (curr_x >= 0 and curr_x < len(grid) and curr_y >= 0 and curr_y < len(grid[0]) 
                    and grid[curr_x][curr_y] == 1 and (curr_x, curr_y) not in visited):
                    visited.add((curr_x, curr_y))
                    queue.append((curr_x, curr_y))           
        return count
    
    def decideType(self, grid, x, y):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        for direction in directions:
            dx, dy = direction
            curr_x = x + dx
            curr_y = y + dy
            if curr_x < 0 or curr_x >= len(grid) or curr_y < 0 or curr_y >= len(grid[0]) or grid[curr_x][curr_y] == 0:
                count += 1
        return count
            
