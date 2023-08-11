class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = defaultdict(int)
        d[0] = 1

        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    d[i] = d[i] + d[i - c]

        return d[amount]
