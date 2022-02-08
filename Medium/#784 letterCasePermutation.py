class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        chars = []

        for char in s:
            if char.isalpha():
                chars.append((char.lower(), char.upper()))
                continue
            else:
                chars.append(char)

        # Now I should have a list of characters being [('a', 'A'), '1', ('b', 'B'), '2']

        # We begin with an empty list
        answer = [[]]

        # Here char is taking over the values ('a', 'A'), '1', ('b', 'B'), '2'
        for char in chars:
            # For every iteration of curr in answer, we are adding the different variants of c in there, either upper case or lower case
            answer = [curr + [c] for curr in answer for c in char]

        return [''.join(ans) for ans in answer]
