class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = set(words[0])

        freqs = [Counter(w) for w in words]

        ans = []

        for char in s:
            ans += [char] * min(f.get(char, 0) for f in freqs)
        
        return ans
        