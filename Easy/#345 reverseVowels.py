class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        stack = []

        for char in s:
            if char in vowels:
                stack.append(char)

        ans = ''

        for char in s:
            if char in vowels:
                ans += stack.pop()

            else:
                ans += char

        return ans
