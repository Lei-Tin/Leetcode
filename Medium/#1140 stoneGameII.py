class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Accumulate sums of the piles
        # Serves as the total number of possible stones a player can get on index i
        for i in range(len(piles) - 1, 0, -1):
            piles[i - 1] += piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, m: int):
            # This is the case when the current player can just take away everything
            if i + 2 * m >= len(piles):
                return piles[i]

            # To maximize current player's gain
            # Take all possible until piles[i] and then remove the minimum that the other player could have gotten
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)
