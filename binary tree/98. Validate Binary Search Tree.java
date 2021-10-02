/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // O(n), S(n)
    public boolean isValidBST(TreeNode root) {
        // The initial lower bound should be MIN_VALUE and upper bound be MAX_VALUE
        // In this way the result will not be effected by initial setting. 
        return decide(root, null, null);
    }
    
    private boolean decide(TreeNode root, Integer low, Integer high) {
        // empty tree is a valid BST.
        if (root == null) return true;
        
        // if the root value is greater than upper bound or smaller than lower bound -> not a BST.
        if ((high != null && root.val >= high) || (low != null && root.val <= low)) return false;
        
        // left and right child trees must be BST, too.
        return decide(root.left, low, root.val) && decide(root.right, root.val, high);
    }
}
