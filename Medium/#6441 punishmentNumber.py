# Wasn't able to do this question in time
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.canPart(str(i * i), i):
                ans += i * i

            # res = []
            # self.part(str(i * i), [], res)
            #
            # for part in res:
            #     if sum(int(c) for c in part) == i:
            #         ans += i * i
            #         break

        return ans

    def part(self, s: str, p: list, res: list) -> None:
        res.append(p + [s])

        for i in range(1, len(s)):
            self.part(s[i:], p + [s[:i]], res)

    def canPart(self, s: str, target: int) -> bool:
        if s == '' and target == 0:
            return True
        if target < 0:
            return False

        for i in range(len(s)):
            left = s[:i]
            right = s[i:]

            if self.canPart(left, target - self.int(right)):
                return True

        return False

    def int(self, s: str) -> int:
        if s == '':
            return 0
        return int(s)

    # Since the input is limited from 1 to 1001, we can actually precompute all the numbers
    # Then we can just create a set to check if the index is within the precomputed set
    def compute(self, n: int) -> List[int]:
        final = []

        for i in range(1, n + 1):
            parts = []
            self.part(str(i * i), [], parts)

            for part in parts:
                if sum(int(c) for c in part) == i:
                    final.append(i)
                    break

        return final
