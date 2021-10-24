class Solution:

    # evaluates LSB each time
    def hammingWeight(self, n: int) -> int:
        total = 0
        while (n!=0):
            total+=1
            n = n & (n-1)
        return total
