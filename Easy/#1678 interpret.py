class Solution:
    def interpret(self, command: str) -> str:
        ans = ''

        i = 0
        while i < len(command):
            if command[i] == '(':
                if command[i + 1] == ')':
                    ans += 'o'
                    i += 2
                else:
                    ans += 'al'
                    i += 4

            else:
                ans += command[i]
                i += 1

        return ans
