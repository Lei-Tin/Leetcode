# Wasn't able to solve this in time
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10 ** 9 + 7

        def f(s: str) -> int:

            # Using DFS to fill in the number from the minimum 000
            # All the way up to maximum, which is s itself.
            @cache
            def dfs(i: int, curr: int, is_limit: bool) -> int:
                # Base case
                if curr > max_sum:
                    return 0
                if i == len(s):
                    return int(curr >= min_sum)

                ans = 0
                limit = int(s[i]) if is_limit else 9

                for j in range(limit + 1):
                    ans += dfs(i + 1, curr + j, is_limit and j == limit)

                return ans % mod

            return dfs(0, 0, True)

        # Converting the problem from possible nums from n1 to n2 into:
        # Possible nums from 0 to n2 -> f(n2)
        # Possible nums from 0 to n1 -> f(n1)
        # So the result is f(n2) - f(n1) + if n1 is valid or not
        return (f(num2) - f(num1) + int(min_sum <= sum(int(c) for c in num1) <= max_sum)) % mod
