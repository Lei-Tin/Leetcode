class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0

        # Iterate from left to right
        left = right = 0

        # This is to count the number of valid parenthesis using the left to right orientation
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1

            if left == right:
                count = max(count, left + right)

            if right > left:
                left = right = 0

        # Iterate from right to left
        left = right = 0

        # This is to count the number of valid parenthesis using the right to left orientation
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1

            if left == right:
                count = max(count, left + right)

            if right < left:
                left = right = 0

        return count
