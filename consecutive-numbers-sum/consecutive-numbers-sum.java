class Solution {
    public int consecutiveNumbersSum(int N) {
        //if(N == 1) return 1;
        
        int ans = 1;
        
        for(int j = 1; (j * (j+1))/2 < N; j++){
            
            if((N - (j * (j + 1)) / 2) % (j+1) == 0){
                
                ans++;
            } 
        }
        
        return ans;
    }
}
