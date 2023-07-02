class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        @cache
        def dfs(i: int, comb: Tuple) -> int:
            if i == len(requests):
                return 0 if all(b == 0 for b in comb) else -inf

            new_comb = list(comb)

            new_comb[requests[i][0]] -= 1
            new_comb[requests[i][1]] += 1

            return max(dfs(i + 1, comb), 1 + dfs(i + 1, tuple(new_comb)))

        return dfs(0, tuple(0 for _ in range(n)))

