class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # [a, b]
        # [d, e]
        # [a ^ d, a ^ e, b ^ d, b ^ e]
        # [a ^ d ^ a ^ e ^ b ^ d ^ b ^ e]

        # [a, b, c]
        # [d, e]
        n1 = len(nums1)
        n2 = len(nums2)

        # If n2 is even, then all numbers in n1 doesnt matter
        # If n1 is even, then all numbers in n2 doesnt matter
        xor_n1 = 0
        xor_n2 = 0
        for num in nums1:
            xor_n1 ^= num

        for num in nums2:
            xor_n2 ^= num

        ans = 0
        if n1 % 2 == 1:
            ans ^= xor_n2
        if n2 % 2 == 1:
            ans ^= xor_n1

        return ans