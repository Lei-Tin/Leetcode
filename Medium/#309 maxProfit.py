class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, can_buy):
            # Max profit until index i with can_buy
            if i >= n:
                return 0

            if can_buy:
                take = dfs(i + 1, False) - prices[i]  # Buy this, cannot buy the next
                not_take = dfs(i + 1, True)

                return max(take, not_take)
            else:
                # Sell at current
                # Cannot buy again next, so have to skip 2
                sell = dfs(i + 2, True) + prices[i]
                not_sell = dfs(i + 1, False)

                return max(sell, not_sell)

        return dfs(0, True)