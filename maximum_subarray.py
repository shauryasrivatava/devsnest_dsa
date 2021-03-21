class Solution(object):
    def maxSubArray(self, nums):
        max_num=max(nums)
        if max_num<0:
            return max_num;
        curr_sum=0
        max_sum=0
        for i in nums:
            curr_sum += i
            if max_sum<curr_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum       
                
