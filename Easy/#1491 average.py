class Solution:
    def average(self, salary: List[int]) -> float:
        minSal, maxSal = 10 ** 6 + 1, 999

        ans = 0

        for s in salary:
            if s < minSal:
                minSal = s

            if s > maxSal:
                maxSal = s

            ans += s

        return (ans - maxSal - minSal) / (len(salary) - 2)
