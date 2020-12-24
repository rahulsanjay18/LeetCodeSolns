class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0;
        int r = people.length - 1;
        int boats = 0;
        while(r >= 0 && people[r] >= limit){
            r--;
            boats++;
        }
        
        while(r >= l){
            if(people[r] + people[l] > limit){
                r--;
                boats++;
            }else{
                l++;
                r--;
                boats++;
            }
        }
        
        return boats;
    }
}
