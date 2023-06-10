class Solution:
    def isFascinating(self, n: int) -> bool:
        ans = str(n)
        if '0' in ans:
            return False

        seen = set()
        n1 = n * 2
        n2 = n * 3

        ans += str(n1)
        ans += str(n2)

        if len(ans) > 9:
            return False

        if '0' in str(n1) or '0' in str(n2):
            return False

        for char in ans:
            if char == '0':
                return False

            seen.add(char)

        return len(seen) == 9
