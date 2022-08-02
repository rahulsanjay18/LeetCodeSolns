class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        
        for i in range(len(magazine)):
            if magazine[i] in dic:
                dic[magazine[i]] += 1
            else:
                dic[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in dic:
                dic[ransomNote[i]] -= 1
                if dic[ransomNote[i]] == 0:
                    del dic[ransomNote[i]]
            else:
                return False
        
        return True