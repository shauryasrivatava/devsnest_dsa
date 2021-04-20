# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def check(root,l,r):
    if root is None:
        return True
    v=root.val
    return v>l and v<r and check(root.left,l,v) and check(root.right,v,r)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inf= (2<<31)+1
        return check(root,-inf,inf)
