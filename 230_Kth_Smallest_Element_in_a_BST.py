def inorder(root,k):
        if root :
            inorder(root.left,k)
            k.append(root.val)
            inorder(root.right,k)
            return k
class Solution:
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans=[]
        inorder(root,ans)
        # print (ans)
        return ans[k-1]
        
#         ANOTHER SOLUTION optimized
class Solution:
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        found=None
        c=0
        def inorder(root):
            if root :
                inorder(root.left)
                nonlocal found
                nonlocal c
                c+=1
                if k==c:
                    found =root
                if found is not None:
                    return 
                inorder(root.right)
        inorder(root)
        return found.val
