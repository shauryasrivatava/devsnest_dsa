class Solution(object):
    def removeDuplicates(self, S):
        stack=[]
        for i in S:
            if len(stack)==0:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            elif i!=stack[-1]:
                stack.append(i)
        return "".join(stack)        
        
