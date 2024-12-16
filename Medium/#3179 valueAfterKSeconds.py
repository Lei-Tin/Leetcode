class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        pref = [1 for _ in range(n)]
        MOD = 10 ** 9 + 7

        for i in range(k):
            for j in range(1, n):
                pref[j] += pref[j - 1] % MOD

        return pref[-1] % MOD
