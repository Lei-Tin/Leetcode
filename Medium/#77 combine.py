class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        self.DFS(ans, k, [], 1, n)

        return ans

    def DFS(self, ans: List, k: int, comb: List, start: int, end: int) -> None:
        # k is the remaining spaces we have to fill
        if k == 0:
            # If k is 0, then we have obtained a combo with the desired length
            ans.append(comb.copy())
        else:
            for i in range(start, end + 1):
                # Then we try every single number and append it to the current comb
                comb.append(i)

                self.DFS(ans, k - 1, comb, i + 1, end)

                comb.pop()

        return


