class Solution(object):
    def dfs(self,i,isConnected):
        if isConnected[i][i]==0:
            return
        for j in range(len(isConnected)):
            if isConnected[i][j]==1:
                isConnected[i][j]=0
                self.dfs(j,isConnected)
    def findCircleNum(self, isConnected):
        city=0
        for i in range(len(isConnected)):
            if isConnected[i][i]==1:
                self.dfs(i,isConnected)
                city+=1
                
        return city