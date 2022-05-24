class Solution(object):
    def word_to_dict(self, word):
        dic = {}
        
        for c in word:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        return dic
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = self.word_to_dict(s)
        dict_t = self.word_to_dict(t)
        
        return dict_s == dict_t
        