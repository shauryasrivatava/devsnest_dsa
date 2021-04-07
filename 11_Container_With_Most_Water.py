class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        i=0
        j =len(height)-1
        total=(min(height[i],height[j])) * (j-i)
        ans=total
        while i<j:
            print(total)
            if height[i]<height[j]:
               i+=1
               total=(min(height[i],height[j])) * (j-i)
               ans=max(total,ans) 
            else:
               j-=1
               total=(min(height[i],height[j])) * (j-i)  
               ans=max(total,ans)
        return ans
