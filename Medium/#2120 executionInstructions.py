class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        moveDict = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        ans = []

        for i in range(len(s)):

            curr = startPos[:]
            cmd = s[i:]

            j = 0

            while j < len(cmd):

                add = moveDict[cmd[j]]
                curr[0] += add[0]
                curr[1] += add[1]

                if not self.isValid(n, curr):
                    break

                j += 1

            ans.append(j)

        return ans

    def isValid(self, n: int, coord: List[int]) -> bool:
        # Returns if the given location is valid in the current n by n grid.
        return 0 <= coord[0] < n and 0 <= coord[1] < n
