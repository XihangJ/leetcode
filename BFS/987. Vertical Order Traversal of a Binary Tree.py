'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
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
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([(root, 0, 0)])
        while queue:
            n = len(queue)
            tmp_d = {}
            for _ in range(n):
                curr, row, col = queue.popleft()
                self.min_col = min(self.min_col, col)
                if col not in tmp_d: 
                    tmp_d[col] = [curr.val]
                else:
                    tmp_d[col].append(curr.val)
                if curr.left: queue.append((curr.left, row + 1, col - 1))
                if curr.right: queue.append((curr.right, row + 1, col + 1))
            for col in tmp_d:
                curr = tmp_d[col]
                curr.sort()
                if col not in self.d:
                    self.d[col] = curr
                else:
                    for val in curr:
                        self.d[col].append(val)
        count, col = 0, self.min_col
        while count < len(self.d):
            if col in self.d:
                curr = self.d[col]
                res.append(curr)
                count += 1
            col += 1
        return res
