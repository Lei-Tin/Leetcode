class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # m = (sum(rolls) + sum(missing)) / (len(rolls) + n)
        sum_missing = mean * (len(rolls) + n) - sum(rolls)

        each, rem = divmod(sum_missing, n)
        avg = sum_missing / n
        if avg > 6 or avg < 1:
            return []

        ans = [each] * n
        for i in range(rem):
            ans[i] += 1

        return ans
