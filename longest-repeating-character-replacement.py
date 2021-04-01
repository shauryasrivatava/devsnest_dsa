this code shows TLE as its time complexity is O(n^2)
class Solution(object):
    def characterReplacement(self, s, k):
        ans=0  
        king=k
        for i in range(len(s)-1):
            count=1
            c=k
            for j in range(i+1,len(s)):
                if s[i]!=s[j]:
                    if c==0:
                        break
                    else:
                        c-=1
                        count +=1
                        if count>ans:
                            ans=count
                            king=c
                                 
                elif s[i]==s[j]:
                    count+=1
                    if count>ans:
                            ans=count
                            king=c           
            
        for i in range(len(s)-1,0,-1):
            count=1
            c=k
            for j in range(i-1,-1,-1):
                if s[i]!=s[j]:
                    if c==0:
                        break
                    else:
                        c-=1
                        count +=1
                        if count>ans:
                            ans=count
                            king=c
                elif s[i]==s[j]:
                    count+=1
                    if count>ans:
                            ans=count
                            king=c               
        if len(s)-ans==king:
            ans=len(s)
            
        return ans            
                    
