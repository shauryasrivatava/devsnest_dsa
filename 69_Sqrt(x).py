class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(math.sqrt(x))
        
        ans=1
        while (ans*ans)<x:
            ans+=1
        if ans*ans>x:
            ans-=1
        return ans
        
