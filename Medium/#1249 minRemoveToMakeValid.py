class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # This is the stack to store the parentheses
        stack = []

        # Since directly interacting with the string is hard, we will use a list
        lst = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()

                else:
                    lst[i] = ''

        for i in stack:
            lst[i] = ''

        return ''.join(lst)
