class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        '''
        if len(s) != len(t) or len(s) == 0:
            return False
        
        c_map = {}
        b_map = {}
        
        for i in range(len(s)):
            if s[i] not in c_map:
                c_map[s[i]] = t[i]
            if t[i] not in b_map:
                b_map[t[i]] = s[i]
      
        for i in range(len(s)):
            if c_map[s[i]] != t[i] or b_map[t[i]] != s[i]:
                return False
        
        return True
        '''