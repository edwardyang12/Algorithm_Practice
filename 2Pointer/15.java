class Solution {


    // Sort array O(n logn)
    // for each element in sorted array check if theres two elements to the right of it
    // that all sum up to 0 by going left with end pointer if too large and right
    // with start pointer if too small
    // if found loop starts until you find next number thats different
    // O(n^2) time
    // O(n) space
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        Arrays.sort(nums);
          System.out.println(Arrays.toString(nums));
        for(int i =0; i<nums.length; i++){
            if(i!=0 && nums[i]==nums[i-1]){
                 continue;
            }
            List<List<Integer>> twoSum = binary(nums,i);
            output.addAll(twoSum);
        }
        return output;
    }
    public List<List<Integer>> binary(int[] nums, int pointer){
        List<List<Integer>> twoSum = new ArrayList<>();
        int start = pointer+1;
        int end = nums.length-1;
        while(start<end){
            int temp = nums[start] + nums[end] + nums[pointer];
            if (temp>0){
                end--;
            }
            else if(temp<0){
                start++;
            }
            else{
                List<Integer> tempList = new ArrayList<>();
                tempList.add(nums[pointer]);
                tempList.add(nums[start]);
                tempList.add(nums[end]);
                twoSum.add(tempList);
                end--;
                start++;
                while(start!=0 && start<nums.length-1 && nums[start]==nums[start-1] ){
                    start++;
                }
            }

        }
        return twoSum;
    }
}
