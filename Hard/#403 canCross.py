class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        goal = stones[-1]

        @cache
        def dfs(i: int, k: int) -> bool:
            if i == goal:
                return True

            if i not in stones_set:
                return False

            if k <= 0:
                return False

            if i > goal:
                return False

            return dfs(i + k - 1, k - 1) or dfs(i + k, k) or dfs(i + k + 1, k + 1)

        return dfs(1, 1)
