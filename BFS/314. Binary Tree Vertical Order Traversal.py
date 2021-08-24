'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #method 1. BFS.
    def __init__(self):
        self.min_col = inf
        self.d = {}
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([(root, 0, 0)])
        while queue:
            n = len(queue)
            for _ in range(n):
                curr, row, col = queue.popleft()
                self.min_col = min(self.min_col, col)
                if col not in self.d: 
                    self.d[col] = [curr.val]
                else:
                    self.d[col].append(curr.val)
                if curr.left: queue.append((curr.left, row + 1, col - 1))
                if curr.right: queue.append((curr.right, row + 1, col + 1))
        count, col = 0, self.min_col
        while count < len(self.d):
            if col in self.d:
                curr = self.d[col]
                res.append(curr)
                count += 1
            col += 1
        return res
