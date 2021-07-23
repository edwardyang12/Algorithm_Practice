class Solution:

    # keep running largest profit
    # if there is a larger i, then take it because largest future profit is with largest i
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        large = prices[len(prices)-1]
        i = len(prices)-1
        while(i>=0):
            if large-prices[i]>currMax:
                currMax = large-prices[i]
            elif prices[i]>large:
                large = prices[i]
            i-=1
        return currMax
