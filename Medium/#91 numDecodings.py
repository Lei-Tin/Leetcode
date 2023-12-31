class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(substr: str) -> int:
            # Dead end
            if len(substr) > 0 and substr[0] == '0':
                return 0

            if not substr:
                return 1

            if 10 <= int(substr[0:2]) <= 26:
                return dfs(substr[1:]) + dfs(substr[2:])
            else:
                return dfs(substr[1:])

        return dfs(s)
