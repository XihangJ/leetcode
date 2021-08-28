'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_max = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(m):
            for col in range(n):
                i, j = row, col
                if grid[i][j] == 1:
                    area = 0
                    queue = collections.deque([(i, j)])
                    grid[i][j] = 0
                    while queue:
                        curr = queue.popleft()
                        area += 1
                        for direction in directions:
                            i, j = curr
                            dx, dy = direction
                            i += dx
                            j += dy
                            if (0 <= i and i < m) and (0 <= j and j < n) and grid[i][j] == 1:
                                queue.append((i, j))
                                grid[i][j] = 0
                    area_max = max(area_max, area)
        return area_max
