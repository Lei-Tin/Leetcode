class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        # Notice that splitting it into k segments is the same as just picking k - 1 adjacent sums
        adjSum = []
        for i in range(n - 1):
            adjSum.append(weights[i] + weights[i + 1])

        adjSum.sort()

        # weights[0] and weights[-1] are always in both, so we can just ignore them
        highest = 0
        lowest = 0

        for i in range(k - 1):
            highest += adjSum[~i]
            lowest += adjSum[i]

        return highest - lowest
