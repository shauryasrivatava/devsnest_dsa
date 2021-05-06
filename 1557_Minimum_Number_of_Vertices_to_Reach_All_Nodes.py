class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        tcounts=[[0,0] for i in range(n)]
        for s,d in edges:
            tcounts[s][1]+=1
            tcounts[d][0]+=1
        ans=[]
        for i in range(n):
            if tcounts[i][0]==0:
                ans.append(i)
        return ans
