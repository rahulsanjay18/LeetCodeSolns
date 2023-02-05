class Solution:
    def climbStairs(self, n: int) -> int:
        last, sec = 1,1
        for i in range(n-1):
            temp = last
            last += sec
            sec = temp
            
        return last
            