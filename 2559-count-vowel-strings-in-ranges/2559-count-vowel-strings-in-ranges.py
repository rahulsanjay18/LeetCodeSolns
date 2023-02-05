class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        ans = []
        prefix = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        good = {i for i in range(len(words)) if words[i][0] in vowels and words[i][-1] in vowels}
        
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if i in good else 0)
        
        for l,r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        
        return ans