class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Solution 2
        maxVal = -1
        for acc in accounts:
            maxVal = max(sum(acc), maxVal)

        return maxVal

        # richest = 0
        #
        # for acc in accounts:
        #     richest = max(richest, sum(acc))
        #
        # return richest
