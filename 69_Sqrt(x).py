class Solution:
    def mySqrt(self, x: int) -> int:
#         return int(math.sqrt(x))
        
#         ans=1
#         while (ans*ans)<x:
#             ans+=1
#         if ans*ans>x:
#             ans-=1
#         return ans

#         In most efficient Time complexity
        lb=0
        ub=x
        mid=0
        if x==1:
            return 1
        while lb<=ub:
            mid=(lb+ub)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                lb=mid+1
            else:
                ub=mid-1
        return mid   
