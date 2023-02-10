class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        abc
        asdjgblksjadskfjklscccdbfkgakjcdkgsjlk
        '''
        
        subseq = set(s)
        
        i_map = {c : [] for c in subseq}
        
        for i in range(len(t)):
            if t[i] in subseq:
                i_map[t[i]].append(i)
        
        if len(subseq) != len(i_map):
            return False
        
        bound = -1
        for c in s:
            if i_map[c]:
                found = False
                for i in i_map[c]:
                    if i > bound:
                        bound = i
                        found = True
                        break
                if not found:
                    return False
            else:
                return False
        return True
            
        