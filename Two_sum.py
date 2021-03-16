class Solution(object):
    def twoSum(self, nums, target):
        nummap={}
        for i in range (len(nums)):
            num=nums[i]
            if(target- num in nummap):
                return [nummap[target-num],i]
            nummap[num]=i
