class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local = 0
        glob = -10000
        
        for n in nums:
            local = max(n, n + local)
            glob = max(local, glob)
        
        return glob