class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color=[0]*len(graph)
        queue=[]
        for i in range(len(graph)):
            if color[i]==1 or color[i]==-1:
                continue
            queue.append(i)
            color[i]=1
            while queue:
                cur=queue.pop()
                for next in graph[cur]:
                    if color[next]==0:
                        color[next]=-(color[cur])
                        queue.append(next )
                    
                    if color[next]==color[cur]:
                        return False
        return True
