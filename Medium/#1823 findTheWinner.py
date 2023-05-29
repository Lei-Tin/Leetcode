class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Done by simulation

        # p as in people, the list of people
        p = [i for i in range(n)]

        # Remember to add 1 to the final answer
        curr_len = len(p)
        i = 0

        while len(p) > 1:
            i = (i + k - 1) % curr_len
            # Remove that person
            p.pop(i)

            curr_len = len(p)

        return p[0] + 1
