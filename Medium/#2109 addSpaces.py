class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''

        i = 0
        j = 0

        while i < len(s):
            if j < len(spaces) and i == spaces[j]:
                res += ' '
                j += 1
            else:
                res += s[i]
                i += 1

        return res
