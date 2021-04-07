class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis=[]
        hasi={}
        stack=[]
        stack.append(nums2[0])
        for i in range (1,len(nums2)):
            if nums2[i]<=stack[-1]:
                stack.append(nums2[i])
            else:
                while len(stack)!=0 and nums2[i]>stack[-1]:
                    hasi[stack[-1]]=nums2[i]
                    stack.pop() 
                stack.append(nums2[i])
        # while len(stack)!=0:
        #     hasi[stack[-1]]=-1
        #     stack.pop()
        for i in range(len(nums1)):
            if nums1[i] in hasi:
                lis.append(hasi[nums1[i]])
            else:
                lis.append(-1)
        return lis      
            
