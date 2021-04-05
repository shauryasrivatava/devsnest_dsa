class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        first=0
        # return (n*(n+1)/2)-sum(nums)
        for i in range(len(nums)+1):
            first=i^first
        for i in nums:
            first=i^first
        return first    
        
        
