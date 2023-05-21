# Wasn't able to do this question in time
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            res = []
            self.part(str(i * i), [], res)

            for part in res:
                if sum(int(c) for c in part) == i:
                    ans += i * i
                    break

        return ans

    def part(self, s: str, p: list, res: list) -> None:
        res.append(p + [s])

        for i in range(1, len(s)):
            self.part(s[i:], p + [s[:i]], res)
