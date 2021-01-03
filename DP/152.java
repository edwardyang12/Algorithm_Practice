class Solution {

    // keep track of current max and min since multiplying negative by negative results in positive
    // O(n) time
    // O(1) space
    public int maxProduct(int[] nums) {

        int max = nums[0];
        int min = nums[0];
        int result = nums[0];
        for(int i=1;i<nums.length;i++){
            int temp = Math.max(nums[i], Math.max(max*nums[i],min*nums[i]));
            min = Math.min(nums[i],Math.min(max*nums[i],min*nums[i]));

            max = temp;
            result = Math.max(max,result);
        }

        return result;
    }
}
