class Solution {
    public int[] productExceptSelf(int[] nums) {
        int fullNum = 1;
        int num0s = 0;
        for(int num : nums){
            if(num != 0) fullNum *= num;
            else num0s++;
        }
        
        if(num0s == 1){
            for(int i = 0; i < nums.length; i++){
                if(nums[i] == 0){
                    nums[i] = fullNum;
                }else{
                    nums[i] = 0;
                }
            }
        }else if(num0s > 1){
            for(int i = 0; i < nums.length; i++){
                nums[i] = 0;
            }
        }else{
            for(int i = 0; i < nums.length; i++){
                nums[i] = fullNum / nums[i];
            }
        }
        
        return nums;
    }
}
