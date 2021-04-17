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
        class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # head=root
        if root is None:
            return root
        l=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(l)
        return root
    

#        ANOTHER SOLUTION        

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root:
#             root.left,root.right = self.invertTree(root.right) ,self.invertTree(root.left)
#         return root


#       ANOTHER SOLUTION

# def change(root) -> TreeNode:
#             if root is None:
#                 return root
#             change(root.right)
#             change(root.left)
#             root.left,root.right= root.right,root.left
#             return root
            
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root is None:
#             return root 
#         return change(root)
