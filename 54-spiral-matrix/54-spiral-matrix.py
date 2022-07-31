class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        tot = rows * cols
        covered = 0

        max_x = rows
        max_y = cols
        min_x = 0
        min_y = 0
        isRow = True
        isFwd = True
        
        # print(rows, cols)
        # print()
        ans = []
        
        while len(ans) < tot:
            
            # right
            for i in range(min_y, max_y):
                # print(min_x, i)
                ans.append(matrix[min_x][i])
            # print(ans)
            
            if len(ans) >= tot:
                continue
            
            # down
            for i in range(min_x+1, max_x):
                # print(i,max_y-1)
                ans.append(matrix[i][max_y-1])
            
            # print(ans)
            
            if len(ans) >= tot:
                continue
            # left
            for i in range(max_y-2, min_y-1, -1):
                # print(max_x-1,i)
                ans.append(matrix[max_x-1][i])
            # print(ans)
            
            if len(ans) >= tot:
                continue
            min_x += 1
            # right
            for i in range(max_x-2, min_x-1, -1):
                # print(i, min_y)
                ans.append(matrix[i][min_y])
            # print(ans)
            min_y += 1
            max_y -= 1
            max_x -= 1
        
        return ans
            
            
            
                