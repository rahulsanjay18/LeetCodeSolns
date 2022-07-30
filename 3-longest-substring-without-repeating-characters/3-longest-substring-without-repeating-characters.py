from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        j = 1
        highest = 0
        
        while i >= 0 and j <= len(s) and j > i:
            sub = s[i:j]
            if self.isUnique(sub):
                # print("here")
                highest = max(highest, j-i)
                j += 1
            else:
                i += 1
                j += 1
                
        return highest
    
    def isUnique(self, sub):
        return len((Counter(sub)).items()) == len(sub)
            