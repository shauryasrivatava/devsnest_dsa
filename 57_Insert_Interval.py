class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans=[]
        res=[]
        intervals.sort()
        
        for i in range(len(intervals)):
            inter=intervals[i]
            if newInterval[0]<inter[0]:
                ans.append(newInterval)
            ans.append(inter)
        if newInterval not in ans:
            ans.append(newInterval)
        if len(ans)<=1:
            return ans
            
        prev=ans[0]
        for i in range(1,len(ans)):
            inter=ans[i]
            if prev[1]>=inter[0]:
                prev[1]=max(inter[1],prev[1])
                inter=prev
            if prev not in res:
                res.append(prev)
            last=prev
            prev=inter
            
        if last[1]<prev[0]:
            res.append(prev)
            
        return res
