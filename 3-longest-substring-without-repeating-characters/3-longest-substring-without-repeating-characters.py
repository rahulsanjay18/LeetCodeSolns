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
                highest = max(highest, j-i)
                j += 1
            else:
                i += 1
                j += 1
                
        return highest
    
    def isUnique(self, sub):
        return len((Counter(sub)).items()) == len(sub)
    
    
    '''
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            n = len(s)
            ans = 0
            # mp stores the current index of a character
            mp = {}

            i = 0
            # try to extend the range [i, j]
            for j in range(n):
                if s[j] in mp:
                    i = max(mp[s[j]], i)

                ans = max(ans, j - i + 1)
                mp[s[j]] = j + 1

            return ans
    '''