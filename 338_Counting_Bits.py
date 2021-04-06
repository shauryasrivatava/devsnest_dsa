class Solution:
    def countBits(self, num: int) -> List[int]:
        lis=[]
        for i in range(num+1):
            count =0
            
            while i!=0:
                i=i&(i-1)
                count+=1
            lis.append(count)
        return lis  
