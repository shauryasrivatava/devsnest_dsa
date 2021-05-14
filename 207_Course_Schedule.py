class Solution:
    def dfs(self,vis,i,adj):
        # if vis[i] == 1:
        #     return False
        # if vis[i] == 2:
        #     return True
        vis[i]=1
        for j in adj[i]:
            if vis[j]==0 and not self.dfs(vis,j,adj):
                    return False
            elif vis[j]==1:
                return False
        vis[i]=2
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites = collections.defaultdict(list)
        adj=[None]*numCourses
        for i in range(numCourses):
            adj[i]=[]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
            
        vis=[0]*numCourses
        for i in range(numCourses):
            if vis[i]==0:
                if not self.dfs(vis,i,adj):
                    return False
        return True
