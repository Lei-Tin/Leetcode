class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        run = 0
        ans = 0

        for num in gain:
            run += num
            ans = max(ans, run)

        return ans
