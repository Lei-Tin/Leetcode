class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0

        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)

        for i, char in enumerate(word):
            if char in vowels:
                # Choose one index from left of i
                # Choose one index from right of i
                # smallest can go is s[i:i+1]
                # i + 1 choices for left
                # n - i choices for right
                ans += (i + 1) * (n - i)

        return ans
