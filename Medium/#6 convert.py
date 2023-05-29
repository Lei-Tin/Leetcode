class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        # Solution by simulation
        rows = ['' for _ in range(numRows)]

        # Row and direction
        r, d = 0, 1

        for char in s:
            rows[r] += char
            if r == numRows - 1:
                d = -1
            elif r == 0:
                d = 1

            r += d

        return ''.join(rows)
