class Solution(object):
    def helper(self,res,s,opan,close): 
        if opan==0 and close==0:
            res.append("".join(s))
            return
        if opan>0:
            s.append('(')
            self.helper(res,s,opan-1,close)
            s.pop()
        if close>0 and close>opan:
            s.append(')')
            self.helper(res,s,opan,close-1)
            s.pop()
    def generateParenthesis(self, n):
        res=[]
        s=[]
        self.helper(res,s,n,n)
        return res
