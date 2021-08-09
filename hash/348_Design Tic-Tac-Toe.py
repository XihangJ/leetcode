'''
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
Follow up:
Could you do better than O(n2) per move() operation?
'''

class TicTacToe:
    
    #method 2. row and col. O(1), S(n)
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """    
        n = len(self.row)
        if player == 1:
            inc = 1
        else:
            inc = -1
        
        self.row[row] += inc
        self.col[col] += inc
        
        if row == col: self.diagonal += inc
        if row + col == n - 1: self.antidiagonal += inc
        
        print(self.row, self.col, self.diagonal, self.antidiagonal)
        if (self.row[row] == n or self.col[col] == n or self.diagonal == n or self.antidiagonal == n
           or self.row[row] == -n or self.col[col] == -n or self.diagonal == -n or self.antidiagonal == -n):
            return player
        else:
            return 0
    
    
    
    
    '''
    #method 1. Board as matrix. O(n), S(n^2)
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        flag = False
        for i in range(len(self.board)):
            if self.board[i][col] != player: 
                flag = False
                break
            else:
                flag = True
        if flag: return player
        for j in range(len(self.board[0])):
            if self.board[row][j] != player:
                flag = False
                break
            else:
                flag = True
        if flag: return player

        if row == col:
            for i in range(len(self.board)):
                if self.board[i][i] != player:
                    flag = False
                    break
                else:
                    flag = True
            if flag: return player
        if row + col == len(self.board) - 1:
            for i in range(len(self.board)):
                if self.board[i][len(self.board) - 1 - i] != player:
                    flag = False
                    break
                else:
                    flag = True
            if flag: return player
        return 0
    '''

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
