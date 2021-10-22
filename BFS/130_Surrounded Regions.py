'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    
    # BFS. O(n ** 2), S(n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(row, col):
            queue = collections.deque([(row, col)])
            board[row][col] = "s"
            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    dr, dc = direction
                    r = row + dr
                    c = col + dc
                    if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == "O":
                        board[r][c] = "s"
                        queue.append((r, c))
        
        # 1. find safe place (boarder elements)
        # first and last row:
        for col in range(len(board[0])):
            if board[0][col] == "O":
                bfs(0, col)
            if board[-1][col] == "O":
                bfs(len(board) - 1, col)
        # first and last col
        for row in range(len(board)):
            if board[row][0] == "O":
                bfs(row, 0)
            if board[row][-1] == "O":
                bfs(row, len(board[0]) - 1)
        # 2. flip remaining "O" to "X". And flip "s" back to "O"
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "s": board[row][col] = "O"
                elif board[row][col] == "O": board[row][col] = "X"
        return
    
    
    
    
    '''
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
    '''
