class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        log = {}
        length = 0
        single = False
        for c in s:
            if c not in log:
                log[c] = 1
            else:
                log[c] += 1

        # print(log)
        for k in log:
            ct = log[k]
            
            if ct % 2 == 0:
                length += ct
            else:
                
                length += (ct // 2) * 2
                single = True

        if single:
            length += 1

        return length
        