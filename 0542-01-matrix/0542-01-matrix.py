

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        if r == 0:
            return mat
        
        dist = [[r*c for _ in range(c)] for __ in range(r)]
        
        queue = []
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        for i in range(r):
            for j in range(c):
                if (mat[i][j] == 0):
                    dist[i][j] = 0
                    queue.append((i, j))
                    
        while len(queue) > 0:
            curr = queue.pop(0)
            for dir_ in dirs:
                new_r = curr[0] + dir_[0]
                new_c = curr[1] + dir_[1]
                
                if 0 <= new_r < r and 0 <= new_c < c:
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] +  1:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        queue.append((new_r, new_c))
            
        return dist
        
#################### Brute Force ################################################
        
        '''
        r = len(mat)
        c = len(mat[0])
        if r == 0:
            return mat
        dist = [[r*c for _ in range(c)] for __ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    continue
                
                for k in range(r):
                    for l in range(c):
                        if mat[k][l] == 0:
                            d = abs(k - i) + abs(l - j)
                            dist[i][j] = min(dist[i][j], d)
                print(dist)
        return dist
        '''