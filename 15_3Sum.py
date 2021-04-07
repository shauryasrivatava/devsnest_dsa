class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis=[]
        ans=[]
        nums.sort()
        for z in range(len(nums)-2):
            x=z+1
            y=len(nums)-1
            while x<y:
                # print(nums[x]+nums[y])
                if -(nums[z])==(nums[x]+nums[y]):
                    ans.append(nums[x])
                    ans.append(nums[y])
                    ans.append(nums[z])
                    if ans not in lis and ans!=[]:
                        lis.append(ans)
                    if x+1<len(nums) and y-1>-1:
                        x=x+1
                        y=y-1
                    ans=[]    
                if (nums[x]+nums[y])<-nums[z]:
                    x+=1
                    # print(x+y)
                    # print(nums[x]+nums[y])
                    # return [[]]

                elif (nums[x]+nums[y])>-nums[z]:
                    y-=1 
                    # print(x+y)
            if ans not in lis and ans!=[]:
                lis.append(ans)
            # print(ans)     
            ans=[]    
        return lis  
        
