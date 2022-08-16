# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        
        return root
        
        
    def invert(self, root):
        if root is None or not(root.left or root.right):
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invert(root.right)
        self.invert(root.left)