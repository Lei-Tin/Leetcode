class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def hammingWeight(n):
            res = 0
            while n:
                n &= n - 1
                res += 1

            return res

        prev_max = -1
        curr_min = float('inf')
        curr_max = -1

        prev_bit = -1

        for num in nums:
            bit = hammingWeight(num)

            if bit != prev_bit:
                if prev_max > curr_min:
                    return False

                prev_bit = bit
                prev_max = curr_max

                curr_min = num
                curr_max = num
            else:
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)

        if prev_max > curr_min:
            return False

        return True
