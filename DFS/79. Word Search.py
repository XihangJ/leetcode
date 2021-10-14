'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    #method 1. backtracking. O(mn * (3 ** w)), S(w)
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n: return False
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def backtrack(row, col, i, visited):
            if i == len(word) - 1:
                return True
            for direction in directions:
                dr, dc = direction
                r = row + dr
                c = col + dc
                if r >= 0 and r < m and c >= 0 and c < n and board[r][c] == word[i + 1] and (r, c) not in visited:
                    visited.add((r, c))
                    flag = backtrack(r, c, i + 1, visited)
                    if flag: return True
                    visited.remove((r, c))
            return False
        
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    flag = backtrack(row, col, 0, set([(row, col)]))
                    if flag: return True
        return False
