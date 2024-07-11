class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Regular stack solution
        stack = []

        for char in s:
            if char == ')':
                rev = []

                while len(stack) > 0:
                    # Reverse until the first '(' seen in the stack
                    c = stack.pop()

                    if c == '(':
                        # Proceed to processing more characters
                        break

                    rev.append(c)

                stack.extend(rev)
            else:
                stack.append(char)

        return ''.join(stack)

        # Alternative list solution
        # ans = list(s)

        # pairs = []

        # opens = []

        # for i, char in enumerate(s):
        #     if char == '(':
        #         opens.append(i)
        #     elif char == ')':
        #         pairs.append((opens.pop(), i))

        # # The order in pairs is the order that they are closed in
        # for l_idx, r_idx in pairs:
        #     # Reverse those characters in between
        #     ans[l_idx + 1:r_idx] = ans[l_idx + 1:r_idx][::-1]

        # return ''.join(map(lambda x: x if x not in ('(', ')') else '', ans))