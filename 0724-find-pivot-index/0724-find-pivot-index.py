class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sums = sum(nums)
        lhs = 0
        
        
        for i in range(len(nums)):
            if lhs == sums - nums[i] - lhs:
                return i
            
            lhs += nums[i]
        
        return -1