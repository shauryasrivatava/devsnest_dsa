class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in O(n^2)
        # ans=[1]*len(nums)
        # for i in  range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j:
        #             ans[i]*=nums[j]
        # return ans
        
        # in O(n) with division
        # prod=1
        # out=[]
        # c=0
        # j=[]
        # for i in nums:
        #     if i!=0:
        #         prod*=i
        #     else:
        #         j.append(c)
        #     c+=1
        # for i in range(len(nums)):
        #     if len(j)==0:
        #         out.append(int(prod/nums[i]))
        #     elif len(j)>1 or i not in j:
        #         out.append(0)
        #     elif i in j:
        #         out.append(prod)
        # return out
        
        # in O(n) time_complexity and O(1) space
        prod=1
        output=[1]*len(nums)
        for i in range(len(nums)):
            prod*=nums[i]
            output[i]=prod
        prod=1
        for i in range(len(nums)-1,0,-1):
            output[i]=output[i-1]*prod
            prod*=nums[i]
        output[0]=prod
        return output
