class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        c=0
        k=0
        while l<r:
            if c>1:
                break
            if s[l]!=s[r]:
                c+=1
                l+=1
            else :
                l+=1
                r-=1
                
        l=0
        r=len(s)-1        
        while l<r:
            if k>1:
                break
            if s[l]!=s[r]:
                k+=1
                r-=1 
            else:
                l+=1
                r-=1    
        if c<=1 or k<=1:
            return True
        else:
            return False
            
