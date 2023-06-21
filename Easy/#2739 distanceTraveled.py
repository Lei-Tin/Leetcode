class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0

        cnt = 0
        while mainTank > 0:
            cnt += 1
            if cnt == 5:
                cnt = 0
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1

            ans += 10
            mainTank -= 1

        return ans
