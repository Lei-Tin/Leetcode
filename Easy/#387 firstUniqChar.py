class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Solution 3
        cnt = {}
        first_index = {}

        for i in range(len(s)):
            if s[i] not in first_index:
                first_index[s[i]] = i

            cnt[s[i]] = cnt.get(s[i], 0) + 1

        for char in cnt:
            if cnt[char] == 1:
                return first_index[char]

        return -1

        # Solution 1
        #         for i in range(len(s)):
        #             if s[i] not in s[:i] + s[i + 1:]:
        #                 return i

        #         return -1

        # Solution 2
        # seen = {}
        #
        # for char in s:
        #     if char not in seen:
        #         seen[char] = 1
        #     else:
        #         seen[char] += 1
        #
        # for i in range(len(s)):
        #     if seen[s[i]] == 1:
        #         return i
        #
        # return -1
