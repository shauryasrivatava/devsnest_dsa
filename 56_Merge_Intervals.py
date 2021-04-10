class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        prev=intervals[0]
        
        if len(intervals)<=1:
            return intervals
        
        for i in range(1,len(intervals)):
            inter=intervals[i]
            if prev[1]>=inter[0]:
                prev[1]=max(inter[1],prev[1])
                inter=prev
            if prev not in ans:
                ans.append(prev)
            last=prev    
            prev=inter 
            
        if last[1]<prev[0]:
            if prev not in ans:
                ans.append(prev)
                
        return ans
