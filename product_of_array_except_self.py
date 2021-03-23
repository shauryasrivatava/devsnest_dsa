class Solution(object):
    def productExceptSelf(self, nums):
        prod=int(1)
        output= [1]*len(nums)
        if len(nums)<1:
            return output
        for i in range(len(nums)):
            prod=nums[i]*prod
            output[i] =prod
        prod=1    
        for i in range(len(nums)-1,0,-1):
            output[i]=output[i-1]*prod
            prod=prod*nums[i]
        output[0]=prod
        return output
