class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #if length of given list "intervals" is less then or equal to one then return 0
        if len(intervals)<=1:
            return 0
        
        # sorting the list "intervals"
        intervals.sort(key=lambda x:x[1])
        
        # logic
        prev=intervals[0]
        count=0
        for i in range(1,len(intervals)):
            inter=intervals[i]
            if prev[1]>inter[0]:
                # prev[1]=max(prev[1],inter[1])
                inter=prev
                count+=1
            last=prev
            prev=inter
        
#         if last[1]>inter[0]:
#             count+=1
        return count
