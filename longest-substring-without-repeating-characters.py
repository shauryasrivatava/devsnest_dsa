# in O(n) time complexity
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        setchar=set()
        l=0
        r=0
        ans=0
        while r<len(s):
            if s[r] in setchar:
                while s[l]!=s[r]:
                    setchar.remove(s[l])
                    l+=1
                l=l+1    
            else:
                setchar.add(s[r])
                ans=max(ans,len(setchar))
            r+=1
        return ans   
