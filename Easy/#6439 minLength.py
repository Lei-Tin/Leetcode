class Solution:
    def minLength(self, s: str) -> int:
        temp = ''
        for i in range(len(s)):
            temp += s[i]

            if len(temp) >= 2:
                if temp[-2:] in {'AB', 'CD'}:
                    temp = temp[:-2]

        return len(temp)
