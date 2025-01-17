class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def cond(w):
            return w[0] in vowels and w[-1] in vowels

        n = len(words)
        pref = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            pref[i] = pref[i - 1]

            if cond(words[i - 1]):
                pref[i] += 1

        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] - pref[l])

        return ans