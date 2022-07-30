class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}
        
        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1
                
            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
                
        return s_hash == t_hash