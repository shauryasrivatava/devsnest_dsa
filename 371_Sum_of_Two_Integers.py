class Solution(object):
    def getSum(self, a, b):
        xor=a^b
        annd=a&b
        return (xor+(annd<<1))
