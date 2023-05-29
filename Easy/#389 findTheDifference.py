class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Using XOR to find the only character that is not duplicated
        val = 0
        for char in s:
            val ^= ord(char)

        for char in t:
            val ^= ord(char)

        return chr(val)
