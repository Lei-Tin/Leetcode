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


# Another solution, runtime is slower
# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         # Player 1 is Alice, 0 is Bob
#         @lru_cache(maxsize=None)
#         def dp(i: int, m: int, player: int):
#             if i >= len(piles):
#                 return 0
#
#             # If we are playing as the player, we want to maximize the sum of these piles
#             # From i to i + x, then combined with the gain after we took x piles
#             if player:
#                 return max(sum(piles[i:i + x]) + dp(i + x, max(m, x), 1 - player) for x in range(1, 2 * m + 1))
#             else:
#                 # If we are not the player, we try to minimize the amount that the player can get
#                 return min(dp(i + x, max(m, x), 1 - player) for x in range(1, 2 * m + 1))
#
#         return dp(0, 1, 1)
