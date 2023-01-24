class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Looking for patterns
        # We have 4 total cases

        # start is odd, end is odd, 1, 5
        # 1, 3, 5
        # = (5 - 1) / 2 + 1

        # start is odd, end is even, 1, 4
        # 1, 3
        # = (4 - 1) // 2 + 1

        # start is even, end is odd, 2, 5
        # 3, 5
        # = (5 - 2) // 2 + 1

        # start is even, end is even, 2, 4
        # 3
        # = 4 - 2 // 2

        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        return (high - low) // 2 + 1
