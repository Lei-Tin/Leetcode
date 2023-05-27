class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Player 1 is Alice
        # Player 0 is Bob
        # Returns the difference between Alice's points and Bob's points
        @lru_cache(maxsize=None)
        def dp(i: int, player: int) -> Tuple[int, int]:
            if i >= len(stoneValue):
                return 0

            # For Alice, the points are positive
            if player:
                return max(sum(stoneValue[i:i + x]) + dp(i + x, 1 - player) for x in range(1, 4))
            else:
                # For Bob, all points earned is negative points for Alice
                return min(-sum(stoneValue[i:i + x]) + dp(i + x, 1 - player) for x in range(1, 4))

            return ans

        a = dp(0, 1)
        if a > 0:
            return 'Alice'
        elif a < 0:
            return 'Bob'
        else:
            return 'Tie'

