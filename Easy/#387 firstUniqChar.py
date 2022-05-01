class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Solution 1
        #         for i in range(len(s)):
        #             if s[i] not in s[:i] + s[i + 1:]:
        #                 return i

        #         return -1

        # Solution 2
        seen = {}

        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1
