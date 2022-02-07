class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        for i in range(len(words)):
            s = ''

            for j in range(len(words[i]) - 1, -1, -1):
                s += words[i][j]

            words[i] = s

        return ' '.join(words)
