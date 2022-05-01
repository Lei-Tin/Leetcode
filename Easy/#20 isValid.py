class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)

            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False

            else:
                continue

        return stack == []
