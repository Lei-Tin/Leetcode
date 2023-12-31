class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        if n == 1:
            return 0

        l, r = 0, 1
        ans = 0

        while r < n:
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    ans += neededTime[l]
                    l, r = r, r + 1
                else:
                    ans += neededTime[r]
                    r += 1

            else:
                l, r = r, r + 1

        return ans
