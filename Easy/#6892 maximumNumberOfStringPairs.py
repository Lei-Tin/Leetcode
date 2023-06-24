class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        #         used = set()
        #         n = len(words)
        #         for i in range(n):
        #             w1 = words[i]
        #             for j in range(i + 1, n):
        #                 w2 = words[j]
        #                 if not(i in used or j in used):
        #                     if w1[::-1] == w2:
        #                         used.add(i)
        #                         used.add(j)

        #         return len(used) // 2

        s = set()
        ans = 0

        for w in words:
            if w[0] != w[1]:
                if w[1] + w[0] in s:
                    s.discard(w[1] + w[0])
                    ans += 1
                else:
                    s.add(w[0] + w[1])

        return ans
