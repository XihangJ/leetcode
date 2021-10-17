'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''

class Solution:
    #method 2. DFS2. O(n), S(n)
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] != -1:
            if arr[start] == 0: return True
            curr = arr[start]
            arr[start] = -1
            return self.canReach(arr, start - curr) or self.canReach(arr, start + curr)
        return False
    
    
    '''
    #method 1. DFS. O(n), S(n)
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        visited = set([start])
        
        def dfs(start):
            if arr[start] == 0: return True
            if len(visited) == n: return False
            if (start + arr[start] < n and start - arr[start] >= 0 and 
                start + arr[start] not in visited and start - arr[start] not in visited):
                visited.add(start + arr[start])
                visited.add(start - arr[start])
                return dfs(start + arr[start]) or dfs(start - arr[start])
            elif start + arr[start] < n and start + arr[start] not in visited:
                visited.add(start + arr[start])
                return dfs(start + arr[start])
            elif start - arr[start] >= 0 and start - arr[start] not in visited:
                visited.add(start - arr[start])
                return dfs(start - arr[start])
            return False
        
        return dfs(start)
    '''
