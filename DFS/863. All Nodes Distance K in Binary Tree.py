'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#method 1. DFS + BFS. O(N), S(N)
class Solution:    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return []
        if not target: return []
        self.findParent(root, None)
        queue = collections.deque([target])
        visited = set([target])
        layer = 0
        res = []
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if layer == k:
                    res.append(curr.val)    
                else:
                    if curr.left and curr.left not in visited:
                        queue.append(curr.left)
                        visited.add(curr.left)
                    if curr.right and curr.right not in visited:
                        queue.append(curr.right)
                        visited.add(curr.right)
                    if curr.parent and curr.parent not in visited:
                        queue.append(curr.parent)
                        visited.add(curr.parent)
            layer += 1
        return res
        
    def findParent(self, root, parent):
        if root:
            root.parent = parent
            self.findParent(root.left, root)
            self.findParent(root.right, root)
        return
