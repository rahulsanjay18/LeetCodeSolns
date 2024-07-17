class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def dfs(s, ct=0):
            if ct == n:
                ans.append(s)
                return

            if ct > 0 and s[-1] == "0":
                dfs(s+"1", ct + 1)
            else:
                dfs(s+"1", ct + 1)
                dfs(s+"0", ct + 1)
        
        dfs('')

        return ans