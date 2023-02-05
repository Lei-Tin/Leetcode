class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Solution 1 - Brute Force
        # word = tuple(sorted(p))
        # i = 0

        # ans = []

        # while i + len(p) - 1 < len(s):
        #     if tuple(sorted(s[i:i + len(p)])) == word:
        #         ans.append(i)

        #     i += 1

        # return ans

        # Solution 2 - Using hashmaps with counter
        if len(p) > len(s):
            return []

        ans = []
        count_p = {}
        count_window = {}

        for char in p:
            count_p[char] = count_p.get(char, 0) + 1

        for i in range(len(p) - 1):
            count_window[s[i]] = count_window.get(s[i], 0) + 1

        start_idx = 0
        for i in range(len(p) - 1, len(s)):
            # Add the character
            count_window[s[i]] = count_window.get(s[i], 0) + 1
            if count_window == count_p:
                ans.append(start_idx)

            # Drop the last character
            count_window[s[i - len(p) + 1]] -= 1
            if count_window[s[i - len(p) + 1]] == 0:
                del count_window[s[i - len(p) + 1]]

            start_idx += 1

        return ans
