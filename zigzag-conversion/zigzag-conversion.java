class Solution {
    public String convert(String s, int numRows) {
        
        if(s.length() < 3 || numRows ==  1){
            return s;
        }
        
        //Get First String
        int length = s.length();
        StringBuilder finalAns = new StringBuilder(length);
        int endSkipLength = 2 * numRows - 2;
        int diagSkip = 0;
        int colSkip = 0;
        
        
        for(int i = 0; i < length; i += endSkipLength){
            finalAns.append(s.charAt(i));
        }
        
        for(int i = 1; i < numRows - 1; i++){
            
            diagSkip = endSkipLength - 2 * i;
            colSkip = endSkipLength - diagSkip;
            
            for(int j = i; j < length; j += colSkip){
                finalAns.append(s.charAt(j));
                j += diagSkip;
                if(j < length){
                    finalAns.append(s.charAt(j));
                }
            }
            
            
        }
        
        for(int i = numRows - 1; i < length; i += endSkipLength){
            finalAns.append(s.charAt(i));
        }
        
        return finalAns.toString();
    }
}
