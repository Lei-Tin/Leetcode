class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        index_one = nums.index(1)
        index_n = nums.index(n)

        if index_one == 0 and index_n == n - 1:
            return 0

        if index_n > index_one:
            # 2, 1, 4, 3
            # Return 1 + (4 - 2) - 1 = 2
            return index_one + n - index_n - 1
        elif index_one > index_n:
            # 4, 3, 2, 1
            # Return 3 + (4 - 0) - 2
            return index_one + n - index_n - 2
