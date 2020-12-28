class Solution {

    //
    // first get last occurrence of each character since that will be last place we need it
    // go through S and everytime we see Character for first time we add to HashSet
    // if the index we're at is the same as ending index we remove character from HashSet
    // if HashSet empty we add the part the size to ArrayList
    // O(n) time
    // O(1) space [at most 26 characters]
    public List<Integer> partitionLabels(String S) {
        HashMap<Character, Integer> include = new HashMap<Character, Integer>();
        ArrayList<Integer> parts = new ArrayList<Integer>();
        for(int i=S.length()-1; i>=0; i--){
            if (!include.containsKey(S.charAt(i))){
                include.put(S.charAt(i),i);
            }
        }

        HashSet<Character> contain = new HashSet<Character>();
        int pointer =0;
        for(int i=0; i<S.length(); i++){
            if(include.get(S.charAt(i))==i){
                contain.remove(S.charAt(i));
                if(contain.size()==0){
                    parts.add(i+1-pointer);
                    pointer = i+1;
                }
            }
            else if(!contain.contains(S.charAt(i))){
                contain.add(S.charAt(i));
            }
        }
        return parts;

    }
}
