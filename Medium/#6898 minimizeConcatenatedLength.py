# Wasn't able to finish in time
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @cache
        def dp(i: int, f1: str, l1: str) -> int:
            if i >= len(words):
                return 0

            f2, l2 = words[i][0], words[i][-1]
            if l1 == f2:
                left_right = len(words[i]) + dp(i + 1, f1, l2) - 1
            else:
                left_right = len(words[i]) + dp(i + 1, f1, l2)

            if l2 == f1:
                right_left = len(words[i]) + dp(i + 1, f2, l1) - 1
            else:
                right_left = len(words[i]) + dp(i + 1, f2, l1)

            return min(left_right, right_left)

        return dp(1, words[0][0], words[0][-1]) + len(words[0])

