class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in cols:
                matrix[i][j] = 0