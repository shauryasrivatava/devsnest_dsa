class Solution(object):
    def isAnagram(self, s, t):
        # return ''.join(sorted(s))==''.join(sorted(t))
        d={}
        for i in s:
            if i in d:
                d[i] +=1
            else:
                d[i]=1
        for i in t:
            if i not in d:
                return False
            if d[i]<=0:
                return False
            if i in d:
                d[i] -=1
        for i in d:
            if d[i]!=0:
                return False    
        return True
            
