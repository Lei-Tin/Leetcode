class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 0
        j = 1
        n = len(s)

        while j < n:
            curr = s[i:j]
            if s == curr * (n // len(curr)):
                return True

            j += 1

        return False
