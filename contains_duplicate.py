class Solution(object):
    def containsDuplicate(self, nums):
        
        # for i in range (len(nums)):
        #     for j in range (len(nums)):
        #         if (i!=j and nums[i]==nums[j]):
        #             return True
        # return False
        
        # nums.sort()
        # for i in range (1,len(nums)):
        #     if nums[i-1]== nums[i]:
        #         return True
        # return False  
        
        # return len(nums)!=len(set(nums))
        #via hashing
        d={}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False        
        
