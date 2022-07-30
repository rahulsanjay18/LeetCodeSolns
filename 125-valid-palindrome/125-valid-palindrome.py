class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        a = ord('a')
        zero = ord('0')
        s = s.lower()
        
        while j > i:
            end = s[j]
            start = s[i]
            
            if not (0 <= (ord(end) - a) < 26 or 0 <= (ord(end) - zero) < 10):
                j -= 1
                continue
            if not (0 <= (ord(start) - a) <= 26 or 0 <= (ord(start) - zero) < 10):
                i += 1
                continue
            # print(start, end)
            if end != start:
                return False
            else:
                j -= 1
                i += 1
        
        return True