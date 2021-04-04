class Solution(object):
    def subsetsWithDup(self, nums):
        ans=[[]]
        y=[]
        for num in nums:
            for i in ans:
                y+=[[num]+i]
            ans+=y
            y=[]
        prefinal=[]   
        for i in ans:
            i=sorted(i)
            prefinal.append(i)
        final=[]
        for x in prefinal:
            if x not in final:
                final.append(x)
        return final        
        
