class Solution:
    # hashmap to store all values that have been passed over already
    # if target- curr has already been seen, we know that's the correct sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            if target-nums[i] in temp:
                return [temp[target-nums[i]],i]
            else:
                temp[nums[i]] = i
            
