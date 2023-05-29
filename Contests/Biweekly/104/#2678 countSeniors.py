class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for s in details:
            if int(s[-4:-2]) > 60:
                ans += 1

        return ans
