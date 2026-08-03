# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

        #Both are on different side
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root

        #p = root or q = root 
        if p.val == root.val or q.val == root.val:
            print("one is same")
            return root
        
        #Both are on left side
        if p.val < root.val and q.val < root.val:
            print("Both are on left side")
            return self.lowestCommonAncestor(root.left, p, q)
    
        #Both are on right side
        if p.val > root.val and q.val > root.val:
            print("Both are on right side")
            return self.lowestCommonAncestor(root.right, p, q)        
        