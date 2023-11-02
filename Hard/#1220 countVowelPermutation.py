class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1

        for j in range(n - 1):
            # a can only be followed after e, i, u
            new_a = (e + i + u) % MOD

            # e can only be followed after a, i
            new_e = (a + i) % MOD

            # i can be followed after e, o
            new_i = (e + o) % MOD

            # o can be followed after i
            new_o = i % MOD

            # u can be followed after i, o
            new_u = (i + o) % MOD

            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

        return (a + e + i + o + u) % MOD
