class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums[mid] < target or (target < nums[mid] and nums[mid] > nums[high] and nums[low] < target)
        
        low = 0
        high = len(nums) - 1
        mid = 0
        
        while high >= low:
            mid = (high + low) // 2
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif ((nums[low] <= target <= nums[mid]) or (nums[mid] <= nums[high])) and (target < nums[mid] or target > nums[high]):
                high = mid - 1
            else:
                low = mid + 1
        
        return -1