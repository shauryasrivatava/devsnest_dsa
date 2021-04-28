import heapq
from collections import Counter 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        ans=[]
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
            
        # one line for counting frequency
        # freq=Counter(nums)
        for elt,count in freq.items():
            heapq.heappush(ans,(count,elt))
            if len(ans)==k+1:
                heapq.heappop(ans)
        return [i[1] for i in ans]
