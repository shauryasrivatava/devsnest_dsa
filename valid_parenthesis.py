class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0:
            return False
        arr=[]
        braces={"[" : "]", "{":"}" ,"(": ")"} #map
        for i in s:
            if i in braces:
                arr.append(i)
            elif len(arr) !=0 and i == braces[arr[-1]]:
                arr.pop()
            else:
                return False
        
        # if len(arr) == 0:
        #     return True
        # else:
        #     return False
        # one line code for above statement
        
        return len(arr)==0
