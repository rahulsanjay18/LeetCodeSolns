class Solution {
    public int projectionArea(int[][] grid) {
        int xyArea = 0;
        int yzArea = 0;
        int zxArea = 0;
        for(int i = 0; i < grid.length; i++){
            int max = 0;
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] != 0){
                    xyArea++;
                    max = (grid[i][j] > max) ? grid[i][j] : max;
                }
            }
            
            yzArea += max;
        }
        
        for(int j = 0; j < grid[0].length; j++){
            int max = 0;
            for(int i = 0; i < grid.length; i++){
                max = (grid[i][j] > max) ? grid[i][j] : max;
            }
            zxArea += max;
        }
        return xyArea + yzArea + zxArea;
    }
}
