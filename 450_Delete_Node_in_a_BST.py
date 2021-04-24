class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val==key:
            #1st case- both children absent
            if not root.left and not root.right:
                return None
            #2nd case- One child present only
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            #3rd case- Both left and right child present
            p=root.left
            while p.right:
                p=p.right
            root.val=p.val
            root.left=self.deleteNode(root.left,root.val)
            
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        return root
