class Solution(object):
    def dfs(self,i,vis,ans,adj):
        vis[i]=1
        
        for j in adj[i]:
            if vis[j]==0 and self.dfs(j,vis,ans,adj):
                return True
            elif vis[j]==1:
                return True
        ans.append(i)
        vis[i]=2
        return False
            
    def findOrder(self, num, prereq):
        adj=[None]*num
        for i in range(num):
            adj[i]=[]
        for pre in prereq:
            adj[pre[0]].append(pre[1])
        # vis=[0]*num
        print(adj)
        vis=[]
        for i in range(num):
            vis.append(0)
        ans=[]
        for i in range(num):
            if vis[i]==0 and self.dfs(i,vis,ans,adj):
                return []
        # ans.reverse()
        return ans   
