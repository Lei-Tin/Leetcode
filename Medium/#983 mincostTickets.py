class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # n = len(days)

        # @cache
        # def solve(i, curr_val):
        #     if i >= n:
        #         return 0

        #     # Consider not paying for today, pay at a later day
        #     if days[i] <= curr_val:
        #         not_pay_today = solve(i + 1, curr_val)
        #     else:
        #         not_pay_today = float('inf')  # Must pay today

        #     pay_today = min(
        #         costs[0] + solve(i + 1, days[i]),
        #         costs[1] + solve(i + 1, days[i] + 6),
        #         costs[2] + solve(i + 1, days[i] + 29)
        #     )

        #     return min(not_pay_today, pay_today)

        # return solve(0, 0)

        # Optimized
        days_set = set(days)

        @cache
        def solve(day):
            if day <= 0:
                return 0

            # When this day is not required, we don't have to spend more money
            if day not in days_set:
                return solve(day - 1)

            return min(
                solve(day - 1) + costs[0],
                solve(day - 7) + costs[1],
                solve(day - 30) + costs[2]
            )

        return solve(365)
