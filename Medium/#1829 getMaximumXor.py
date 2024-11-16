class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)

        xor = 0
        for num in nums:
            xor ^= num

        # Max num possible
        max_num = (1 << maximumBit) - 1
        res = []

        for i in range(1, n + 1):
            res.append(max_num - xor)
            xor ^= nums[-i]

        return res
