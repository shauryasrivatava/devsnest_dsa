# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def same(s,t):
    if s is None and t is None :
        return True
    if s is None or t is None:
        return False
    if s and t:
        return s.val == t.val and same(s.left, t.left) and same(s.right, t.right)
    # if s.val!=t.val:
        # return False
    # l=same(s.left,t.left)
    # r=same(s.right,t.right)
    # return l and r
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if same(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
