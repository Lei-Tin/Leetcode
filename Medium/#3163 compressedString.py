class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''

        prev_char = ''
        curr_count = 0

        for char in word:
            if char == prev_char and curr_count < 9:
                curr_count += 1
            else:
                ans += str(curr_count) + prev_char

                prev_char = char
                curr_count = 1

        ans += str(curr_count) + prev_char

        return ans[1:]
