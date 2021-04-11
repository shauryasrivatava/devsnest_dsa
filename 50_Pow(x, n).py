class Solution:
    def myPow(self, x: float, n: int) -> float:
#         this code is optimized later for it shows TLE
        if n==0:
            return 1
        ans=1
        if n==1:
            return x
        if n==-1:
            return (1/x)
        if n%2==0:
            k=0
            
        else:
            k=1
            if n>0:
                n=n-1
            elif n<0:
                n=n+1
        temp=n
        
        n=n/2    
        while n>0:
            n-=1
            ans*=x
        if temp>0 and k==0:    
            ans=ans*ans
            
        if temp>0 and k==1:
            ans=ans*ans*x
        
        while n<0:
            n+=1
            ans*=(1/x)
        if temp<0 and k==0:
            ans=ans*ans
        if temp<0 and k==1:
            ans=ans*ans*(1/x)
        return ans 
#       after optmization
class Solution(object):
    def myPow(self, x, n):
        isnneg , isxneg= n<0, x<0
        x, n= abs(x), abs(n)
        if n == 0: 
            return 1  
        if n == 1: 
            return 1/x if isnneg else x  
        pwr=self.myPow(x, n/2)
        if n%2 == 0: 
            ans= pwr*pwr
        else: 
            ans= pwr*pwr*x
        if x<0 and n%2==1:
            ans=-ans 
        if n<0:
            ans= 1/ans
        return ans
