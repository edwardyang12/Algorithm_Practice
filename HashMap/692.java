class Solution {

    // hashmap to store unique words and their frequencies
    // hashmap to store frequencies and ordered words
    // return first k elements starting from highest frequency
    // O(nlog(n)) time
    // O(n) space
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> frequencies = new HashMap<String, Integer>();
        int max = 0;
        for (String word: words){
            if(frequencies.containsKey(word)){
                int temp = frequencies.get(word);
                frequencies.replace(word,++temp);
                if(++temp > max){
                    max = ++temp;
                }
            }
            else{
                frequencies.put(word,1);
                if(max==0){
                    max = 1;
                }
            }
        }
        HashMap<Integer, PriorityQueue<String>> ordered = new HashMap<Integer, PriorityQueue<String>>();
        for(String i: frequencies.keySet()){
            int temp = frequencies.get(i);
            if(ordered.containsKey(temp)){
                ordered.get(temp).add(i);
            }
            else{
                PriorityQueue<String> pq = new PriorityQueue<String>();
                pq.add(i);
                ordered.put(temp,pq);
            }
        }
        ArrayList<String> result = new ArrayList<String>();
        for(int i =0; i<k;i++){
            if (ordered.containsKey(max) && ordered.get(max).size()!=0){
                result.add(ordered.get(max).poll());
            }
            else{
                max--;
                i--;
            }
        }
        System.out.println(ordered);
        return result;
    }
}
