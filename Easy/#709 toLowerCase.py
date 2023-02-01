class Solution:
    def toLowerCase(self, s: str) -> str:
        # Without using the built in library
        ans = ''
        for char in s:
            val = ord(char)
            # Capital cases is in this range
            if 65 <= val <= 90:
                # Making it lower case
                val += 32
            ans += chr(val)

        return ans
