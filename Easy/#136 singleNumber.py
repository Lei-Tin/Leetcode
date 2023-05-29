class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]

        for i in range(1, len(nums)):
            # XOR is commutative, and if we take XOR of two of the same element, we get 0
            # Therefore, 0 XOR the only element that appears once is the answer
            x = x ^ nums[i]

        return x

