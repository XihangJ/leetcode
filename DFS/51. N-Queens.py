'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

class Solution:
    
    #method 1. Backtracking. O(n!), S(n^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def generateBoard(board):
            curr = []
            for row in board:
                curr.append(''.join(row))
            return curr
        
        def backtrack(row, diagonal, anti_diagonal, cols, board):
            if row == n:
                res.append(generateBoard(board))
                return
            
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if ((curr_diagonal not in diagonal) and 
                    (curr_anti_diagonal not in anti_diagonal) and
                    (col not in cols)):
                    diagonal.add(curr_diagonal)
                    anti_diagonal.add(curr_anti_diagonal)
                    cols.add(col)
                    board[row][col] = 'Q'

                    backtrack(row + 1, diagonal, anti_diagonal, cols, board)

                    diagonal.remove(curr_diagonal)
                    anti_diagonal.remove(curr_anti_diagonal)
                    cols.remove(col)
                    board[row][col] = '.'
        
        backtrack(0, set(), set(), set(), board)
        return res
