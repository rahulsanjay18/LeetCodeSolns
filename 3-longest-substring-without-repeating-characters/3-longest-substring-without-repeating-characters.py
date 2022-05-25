class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 1
        
        big = 0
        
        while j <= len(s):
            if self.isUnique(s[i:j]):
                j += 1
            else:
                big = j - i - 1 if j - i - 1 > big else big
                i += 1
                j = i + big
    
        return j - i - 1 if j - i - 1 > big else big

    
    def isUnique(self, s):
        rec = set()
        for c in s:
            if c in rec:
                return False
            else:
                rec.add(c)
        
        return True