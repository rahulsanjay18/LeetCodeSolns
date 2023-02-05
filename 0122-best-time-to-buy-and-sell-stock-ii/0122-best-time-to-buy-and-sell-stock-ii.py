class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        global_max = 0
        min_so_far = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > min_so_far:
                global_max += prices[i] - min_so_far
            
            min_so_far = prices[i]
            
        return global_max