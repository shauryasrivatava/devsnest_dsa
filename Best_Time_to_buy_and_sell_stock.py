class Solution(object):
    def maxProfit(self, prices):
        mini=10000
        profit=0
        for i in prices:
            if i<mini :
                mini=i
            elif ((i-mini)>profit):
                profit=i-mini
        return profit
