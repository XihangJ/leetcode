'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
class Solution:
    # BFS. O(mn), S(mn)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = collections.deque()
        area_max = 0
        #BFS search with flooding fill
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = 0
                    queue.append((row, col))
                    visited.add((row, col))
                    grid[row][col] = 0
                    area += 1
                    while queue:
                        row_curr, col_curr = queue.popleft()
                        for direction in directions:
                            dr, dc = direction
                            r = row_curr + dr
                            c = col_curr + dc
                            if r >= 0 and r < m and c >= 0 and c < n and (r, c) not in visited and grid[r][c] == 1:
                                queue.append((r, c))
                                visited.add((r, c))
                                grid[r][c] = 0
                                area += 1
                    area_max = max(area, area_max)
        return area_max


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
'''
