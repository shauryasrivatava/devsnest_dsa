class Solution(object):
    def findJudge(self, N, trust):
        if N==1:
            return 1
        tcounts=[[0,0] for i in range(,N+1)]
        for s,d in trust:
            tcounts[s][1]+=1 #outdegree
            tcounts[d][0]+=1 #indegree
        for i in range (1,N+1):
            if tcounts[i][0]==N-1 and tcounts[i][1]==0:
                return i
        return -1
