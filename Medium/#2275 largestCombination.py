class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0

        for i in range(32):
            cnt = 0
            for num in candidates:
                cnt += (num >> i) & 1

            ans = max(ans, cnt)

        return ans