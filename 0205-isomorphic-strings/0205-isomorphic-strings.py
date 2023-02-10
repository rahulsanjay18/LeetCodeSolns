class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(s) == 0:
            return False
        
        c_map = {}
        b_map = {}
        
        for i in range(len(s)):
            if s[i] not in c_map:
                c_map[s[i]] = t[i]
            if t[i] not in b_map:
                b_map[t[i]] = s[i]
        
        new_s = ''
        new_t = ''
        
        for i in range(len(s)):
            new_s += c_map[s[i]]
            new_t += b_map[t[i]]
        
        return new_s == t and new_t == s
        