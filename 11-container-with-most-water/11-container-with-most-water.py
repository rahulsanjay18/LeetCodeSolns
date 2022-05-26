class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height) - 1
        
        ans = 0
        
        while i < j:
            w = j - i
            h = min(height[i], height[j])
            
            ans = ans if ans > w * h else w * h
            
            if h == height[i]:
                i += 1
            else:
                j -= 1
        
        return ans
                
                    
        