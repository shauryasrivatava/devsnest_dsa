# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root ==p or root ==q:
            return root
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if q.val>root.val and p.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
        # also can code
        # while root:
        #     if p.val < root.val > q.val:
        #         root = root.left
        #     elif p.val > root.val < q.val:
        #         root = root.right
        #     else:
        #         return root
