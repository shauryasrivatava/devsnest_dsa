# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        queue=[]
        queue.append(root)
        res=[]
        ans=[]
        while True:
            size=len(queue)
            if(size==0):
                break
            while(size>0):
                temp=queue.pop(0)
                res.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                size-=1
            ans.append(res)
            res=[]
        return ans
