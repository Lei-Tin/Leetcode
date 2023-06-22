class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(i: int, bought: bool) -> int:
            if i >= len(prices):
                return 0

            if bought:
                # Sell operation
                c = dfs(i + 1, not bought) - fee + prices[i]
            else:
                # Buy operation
                c = dfs(i + 1, not bought) - prices[i]

            # Do nothing and continue
            n = dfs(i + 1, bought)

            return max(n, c)

        return dfs(0, False)
