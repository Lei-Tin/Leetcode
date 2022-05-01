class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        i = 0
        j = 1

        lengths = []

        while i < len(s):
            word = s[i]

            while j < len(s) and s[j] not in word:
                word += s[j]
                j += 1

            lengths.append(len(word))

            i += 1
            j = i + 1

        return max(lengths)
