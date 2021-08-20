'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    #method 1. BFS.
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        safe_set = set()
        queue = collections.deque()
        directions = ['>', '<', '^', 'v']
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    if (i, j) not in safe_set:
                        safe_set.add((i, j))
                        queue.append((i, j))
                    while queue:
                        curr = queue.popleft()
                        for direction in directions:
                            end = self.move(board, curr, direction)
                            if end and board[end[0]][end[1]] == 'O' and end not in safe_set:
                                safe_set.add(end)
                                queue.append(end)
        for i in range(m):
            for j in range(n):
                if (i, j) not in safe_set:
                    board[i][j] = 'X'
        return
                        
                        
                        
    def move(self, board, curr, direction):
        x, y = curr
        if direction == '>': y += 1
        elif direction == '<': y -= 1
        elif direction == '^': x -= 1
        elif direction == 'v': x += 1
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return None
        return (x, y)
