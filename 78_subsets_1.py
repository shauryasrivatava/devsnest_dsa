class Solution(object):
    def subsets(self, nums):
        ans = [[]]
        y=[]
        for num in nums:
            for x in ans:
                y += [[num] + x]
            ans+=y
            y=[]
        return ans       
            
        
