class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<String>();
        for(int i = 1; i <= n; i++){
            StringBuilder elem = new StringBuilder();
            
            if(i % 3 == 0) elem.append("Fizz");
            if(i % 5 == 0) elem.append("Buzz");
            if(elem.toString().length() == 0) elem.append(i);
            
            ans.add(elem.toString());
        }
        
        return ans;
    }
}
