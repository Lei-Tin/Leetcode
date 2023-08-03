class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []
        n = len(digits)

        def solve(curr: str, i: int) -> None:
            if i >= n:
                ans.append(curr)
                return

            for char in mapping[digits[i]]:
                solve(curr + char, i + 1)

        solve('', 0)

        return ans
