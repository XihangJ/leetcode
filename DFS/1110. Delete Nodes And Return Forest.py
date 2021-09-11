'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #method 2. DFS. O(n), S(n)
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def removeNodes(root):
            if root.val in to_delete_set:
                if root.left:
                    removeNodes(root.left)
                    if root.left.val not in to_delete_set: res.append(root.left)
                if root.right:
                    removeNodes(root.right)
                    if root.right.val not in to_delete_set: res.append(root.right)
            else:
                if root.left:
                    removeNodes(root.left)
                    if root.left.val in to_delete_set: root.left = None
                if root.right:
                    removeNodes(root.right)
                    if root.right.val in to_delete_set: root.right = None
          
        to_delete_set = set(to_delete)
        res = []
        if root.val not in to_delete_set: res.append(root)
        removeNodes(root)
        return res
    
    '''
    #method 1. BFS. O(n), S(n)
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        queue = collections.deque([root])
        res = []
        if root.val not in to_delete_set: res.append(root)
        while queue:
            node = queue.popleft()
            if node.val in to_delete_set:
                if node.left:
                    queue.append(node.left)
                    if node.left.val not in to_delete_set: res.append(node.left)
                if node.right:
                    queue.append(node.right)
                    if node.right.val not in to_delete_set: res.append(node.right)
            else:
                if node.left: 
                    queue.append(node.left)
                    if node.left.val in to_delete_set: node.left = None
                if node.right:
                    queue.append(node.right)
                    if node.right.val in to_delete_set: node.right = None
        return res
        '''        
