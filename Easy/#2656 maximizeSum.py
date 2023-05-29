class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        val = max(nums)
        ans = val
        k -= 1
        while k > 0:
            val += 1
            ans += val
            k -= 1

        return ans
