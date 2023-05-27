# Wasn't able to finish in time
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Optimized DP
        d = {}
        st = set(dictionary)

        def dp(i: int) -> int:
            if i >= len(s):
                return 0
            if i in d:
                return d[i]

            res = 1 + dp(i + 1)  # The case where none of the substrings matched
            for j in range(i, len(s)):
                if s[i:j + 1] in st:
                    res = min(res, dp(j + 1))

            d[i] = res
            return res

        return dp(0)

    # Unoptimized DFS
    # def __init__(self):
    #     self.minimum = inf
    # def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    #     dp = [0 for _ in range(len(s))]
    #     d = set(dictionary)

    #     def dfs(i: int, curr_extra: int):
    #         if curr_extra >= self.minimum:
    #             return

    #         if i == len(s):
    #             self.minimum = min(self.minimum, curr_extra)
    #             return

    #         for j in range(i, len(s)):
    #             if s[i:j+1] in d:
    #                 dfs(j + 1, curr_extra)

    #         dfs(i + 1, curr_extra + 1)

    #     dfs(0, 0)
    #     return self.minimum

