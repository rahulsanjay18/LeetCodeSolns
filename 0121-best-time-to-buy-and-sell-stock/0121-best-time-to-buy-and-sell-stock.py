class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        current_min = prices[0]
        for p in prices:
            current_min = min(p, current_min)
            ans = max(p - current_min, ans)
        
        return ans