class Solution {

    // hashmap to store prior strings and balance of strings
    // queue to keep track of current string from hashmap
    // case 1: balanced and total length==2*n, then add to output List
    // case 2: balanced but not equal, must add a (
    // case 3: ( is equal to n, must add )
    // case 4: not balanced, ( not equal to n, can add ( or )
    // O(# of possible well-formed parantheses) -> upper bound is 2^(2n) but this is not possible, time
    // O(# of possible well-formed parantheses) -> upper bound is 2^(2n) but this is not possible, space
    public List<String> generateParenthesis(int n) {
        List<String> output = new ArrayList<String>();
        HashMap<String, int[]> dp = new HashMap<String, int[]>();
        List<String> temp = new ArrayList<String>();
        temp.add("(");
        int[] count = {1,0};
        dp.put("(",count);
        while(!temp.isEmpty()){
            String curr = temp.remove(0);
            count = dp.get(curr);
            if (count[0]==n && count[1]==n){
                output.add(curr);
            }
            else{
                int [] newCurr = new int[2];
                if(count[0]==count[1]){
                    temp.add(curr+"(");
                    newCurr[0] = count[0]+1;
                    newCurr[1] = count[1];
                    dp.put(curr+"(",newCurr);
                }
                else if(count[0]==n){
                    temp.add(curr+")");
                    newCurr[1] = count[1]+1;
                    newCurr[0] = count[0];
                    dp.put(curr+")",newCurr);
                }
                else{
                    temp.add(curr+"(");
                    newCurr[0] = count[0]+1;
                    newCurr[1] = count[1];
                    dp.put(curr+"(",newCurr);
                    newCurr = new int[2];
                    newCurr[1] = count[1]+1;
                    newCurr[0] = count[0];
                    temp.add(curr+")");
                    dp.put(curr+")",newCurr);
                }
            }
        }
        return output;
    }
}
