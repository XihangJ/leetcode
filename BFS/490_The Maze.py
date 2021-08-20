'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).
'''
class Solution:
    
    #method 2. BFS.
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set([(start[0], start[1])])
        start, destination = (start[0], start[1]), (destination[0], destination[1])
        queue = collections.deque([start])
        directions = ['>', '<', '^', 'v']
        while queue:
            curr = queue.popleft()
            for direction in directions:
                end = self.goAlong(maze, curr, direction)
                if end == destination:
                    return True
                if end not in visited:
                    visited.add(end)
                    queue.append(end)
        return False           
            
            
            
    def goAlong(self, maze, start, direction):
        dx, dy = 0, 0 
        if direction == '>': dy = 1
        elif direction == '<': dy = -1
        elif direction == '^': dx = -1
        elif direction == 'v': dx = 1
        x, y = start
        while (x >= 0 and x < len(maze)) and (y >= 0 and y < len(maze[0])) and maze[x][y] != 1:
            x += dx
            y += dy
        return (x - dx, y - dy)        
        
    
    
    '''
    #method 1. DFS.
    def __init__(self):
        self.flag = False
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set([(start[0], start[1])])
        return self.dfs(maze, visited, start, destination)
        
    def dfs(self, maze, visited, start, destination):
        if self.flag: return True
        directions = ['>', '<', '^', 'v']
        for direction in directions:
            end = self.goAlong(maze, start, direction)
            if end in visited: continue
            elif end[0] == destination[0] and end[1] == destination[1]: 
                self.flag = True
                break
            else:
                visited.add(end)
                self.dfs(maze, visited, end, destination)
        if self.flag: return True
        else: return False
                
    def goAlong(self, maze, start, direction):
        dx, dy = 0, 0 
        if direction == '>': dy = 1
        elif direction == '<': dy = -1
        elif direction == '^': dx = -1
        elif direction == 'v': dx = 1
        x, y = start
        while (x >= 0 and x < len(maze)) and (y >= 0 and y < len(maze[0])) and maze[x][y] != 1:
            x += dx
            y += dy
        return (x - dx, y - dy)
        '''
