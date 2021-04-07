class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        minimum=min(nums)
        maximum=max(nums)
        if maximum<0:
            return 1
        for i in range(1,maximum+1):
            if i not in nums and i>0:
                return i
        return maximum+1    
