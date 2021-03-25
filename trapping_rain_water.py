class Solution(object):
    def trap(self, height):
        left=[]
        right=[]
        
        if len(height)<=2:
            return 0
          
        left.append(height[0])
        right.append(height[-1])
        
        maxx=height[0]
        for i in range(1,len(height)):
            if maxx<height[i]:
                maxx=height[i]
                left.append(height[i])
            else:
                left.append(maxx)
            
        maxx=height[-1]
        for i in range(len(height)-2,-1,-1):
            if maxx<height[i]:
                maxx=height[i]
                right.insert(0,height[i])
            else:
                right.insert(0,maxx)
        
        res=0
        m=0
        for i in range(len(height)):
            
            m=min(left[i],right[i])
            res +=(m-height[i])
            
        return res 
