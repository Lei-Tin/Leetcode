class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        ans = 0
        for i in range(n // 3):
            ans += piles[1 + 2 * i]

        return ans