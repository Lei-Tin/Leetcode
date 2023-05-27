class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = inf
        found = False

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                cost = prices[i] + prices[j]
                if cost <= money and cost < min_cost:
                    min_cost = cost
                    found = True

        if found:
            return money - min_cost
        else:
            return money
