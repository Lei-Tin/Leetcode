class Solution:
    def minLength(self, s: str) -> int:
        temp = ''
        for i in range(len(s)):
            temp += s[i]

            if len(temp) >= 2:
                if 'AB' == temp[len(temp) - 2:len(temp)] or 'CD' == temp[len(temp) - 2:len(temp)]:
                    temp = temp[:-2]

        return len(temp)
