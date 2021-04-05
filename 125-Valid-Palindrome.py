class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                stri.append(i.lower())
        rever=''.join(stri)
        stri.reverse()
        stri=''.join(stri)
        # print(stri)
        return rever==stri
