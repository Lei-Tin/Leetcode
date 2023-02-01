class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        count = 0
        ans = ''

        while i < len(word1) and j < len(word2):
            if count % 2 == 0:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1

            count += 1

        if i == len(word1):
            ans += word2[j:]
        else:
            ans += word1[i:]

        return ans
