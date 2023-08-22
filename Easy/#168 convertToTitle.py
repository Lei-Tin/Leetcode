class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''

        while columnNumber > 0:
            columnNumber -= 1

            rem = columnNumber % 26
            columnNumber //= 26

            ans = chr(ord('A') + rem) + ans

        return ans
