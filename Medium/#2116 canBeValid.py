class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False  # odd lenths never work

        wild = 0
        op = 0  # num open parentheses
        cl = 0  # num closed parentheses

        # Forward
        for i, char in enumerate(s):
            if locked[i] == '0':
                wild += 1
            else:  # Locked char
                if char == '(':
                    op += 1
                elif char == ')':
                    cl += 1

            # For each iter, we check if it is possible to make it balanced
            if wild + op - cl < 0:
                return False

        # Backward
        wild = 0
        op = 0  # num open parentheses
        cl = 0  # num closed parentheses

        # Backward
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if locked[i] == '0':
                wild += 1
            else:  # Locked char
                if char == '(':
                    op += 1
                elif char == ')':
                    cl += 1

            # For each iter, we check if it is possible to make it balanced
            # Since this is backwards, we check if we can use wildcard as closed
            if wild + cl - op < 0:
                return False

        return True