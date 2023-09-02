class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = {}
        st = set(dictionary)

        @cache
        def dp(i: int) -> int:
            if i >= len(s):
                return 0

            res = 1 + dp(i + 1)  # The case where none of the substrings matched
            for j in range(i, len(s)):
                if s[i:j + 1] in st:
                    res = min(res, dp(j + 1))

            return res

        return dp(0)
