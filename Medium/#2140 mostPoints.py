class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        self.search(questions, dp)

        return dp[0]

    def search(self, questions: List[List[int]], dp: dict) -> None:
        # Need to go from right to left
        for i in range(len(questions) - 1, -1, -1):
            # Points and brainpower
            pt, bp = questions[i]

            if i + 1 > len(questions):
                dp[i] = pt
            else:
                val_solve = dp.get(i + bp + 1, 0)
                val_skip = dp.get(i + 1, 0)
                dp[i] = max(pt + val_solve, val_skip)

    # Failed attempt on recursion
    # Running time exceeded

    # def search(self, questions: List[List[int]], index: int) -> int:
    #     if index >= len(questions):
    #         return 0

    #     points = questions[index][0]
    #     brainpower = questions[index][1]

    #     return max(points + self.search(questions, index + brainpower + 1), self.search(questions, index + 1))
