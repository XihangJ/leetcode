'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
'''

class Solution:
    #method 1. BFS. O(N), S(N)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        color = image[sr][sc]
        image[sr][sc] = newColor
        m, n = len(image), len(image[0])
        visited = set((sr, sc))
        queue = collections.deque([(sr, sc)])
        while queue:
            curr = queue.popleft()
            row, col = curr
            for direction in directions:
                dr, dc = direction
                r = row + dr
                c = col + dc
                if r >= 0 and r < m and c >= 0 and c < n and (r, c) not in visited and image[r][c] == color:
                    visited.add((r, c))
                    queue.append((r, c))
                    image[r][c] = newColor
        return image
