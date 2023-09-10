class Solution:
    def countOrders(self, n: int) -> int:
        """
        1
        P1 D1

        2
        Fix a location for P1 and P2
        Figure out how many places we can insert D1 and D2
        D2 must be after P2, so 1 place

        D1 can be in P1 _ P2 _ D2 _, so 3 place

        3
        P1 P2 P3
        We need to insert D3 at the end, so
        P1 P2 P3 D3

        Then we can insert D2 in
        P1 P2 _ P3 _ D3 _

        We can insert D1 in
        P1 _ P2 _ (D2) _ P3 _ (D2) _ D3 _ (D2) _, however D2 will only be present in one of these places, so that makes the total possibility 5

        Therefore, the pattern is, n! for the location of P1 P2 ... Pn, then multiply by 1 * 3 * 5 * ... * 2n - 1
        """
        MOD = 10 ** 9 + 7

        ans = 1
        for i in range(1, n + 1):
            ans *= i % MOD
            if (2 * i - 1) % 2 != 0:
                ans *= (2 * i - 1) % MOD

        return ans % MOD
