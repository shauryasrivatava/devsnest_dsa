# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dll(root):
    if root is None:
        return None,None
    lh,lt=dll(root.left)
    rh,rt=dll(root.right)
    if lh:
        h=lh
        lt.right=root
        root.left=lt
    else:
        h=root
    if rh:
        t=rt
        rh.left=root
        root.right=rh
    else:
        t=root
    return h,t
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        h,t=dll(root)
        while h.val!=t.val:
            summ=h.val+t.val
            if summ==k:
                return True
            elif summ>k:
                t=t.left
            elif summ<k:
                h=h.right
        return False
