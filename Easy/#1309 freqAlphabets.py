class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ''

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # this 96 is because it shifts 26 to 122, which is 'z'
                ans += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                ans += chr(int(s[i]) + 96)
                i += 1

        return ans
