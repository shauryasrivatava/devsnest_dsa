class Solution(object):
    def maxSubArray(self, nums):
        max_sum=max(nums)
        if max_sum<0:
            return max_sum;
        curr_sum=0
        for i in nums:
            curr_sum+=nums[i]
            if max_sum<curr_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum       
                
