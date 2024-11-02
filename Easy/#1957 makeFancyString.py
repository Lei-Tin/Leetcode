class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''

        last_char = ''
        last_char_count = 0

        for char in s:
            if char != last_char:
                last_char_count = 0

            else:
                last_char_count += 1

            if last_char_count < 2:
                ans += char

            last_char = char

        return ans
