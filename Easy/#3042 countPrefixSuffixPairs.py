class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words[i + 1:]):
                if w2.startswith(w1) and w2.endswith(w1):
                    ans += 1

        return ans