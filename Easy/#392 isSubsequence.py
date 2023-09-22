class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        count = 0

        for i in range(n):
            if count < len(s):
                if s[count] == t[i]:
                    count += 1

        return count == len(s)
