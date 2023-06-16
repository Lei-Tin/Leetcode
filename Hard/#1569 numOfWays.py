class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # This gives MLE
        # mem = {}
        # def combo(n: int, r: int) -> int:
        #     # Return n! / r! (n - r)!
        #     if r == 0 or n == r:
        #         return 1

        #     if (n, r) in mem:
        #         return mem[(n, r)]

        #     ans = combo(n - 1, r - 1) + combo(n - 1, r)
        #     mem[(n, r)] = ans

        #     return ans

        def f(lst: List[int]) -> int:
            m = len(lst)
            if m <= 2:
                return 1

            # We want to preserve relative order between the smaller and the larger lists
            root = lst[0]
            smaller = []
            larger = []

            for num in lst:
                if num > root:
                    larger.append(num)
                elif num < root:
                    smaller.append(num)
                # There's no case for equals becuase this is BST

            # https://math.stackexchange.com/questions/666288/number-of-ways-to-interleave-two-ordered-sequences/666295#666295
            # The link helps realize why this is comb(m - 1, len(larger))
            # Both len(larger) and len(smaller) would work

            # Can choose to use comb from math, or just write up my own comb
            # My own comb gives MLE
            return f(smaller) * f(larger) * comb(m - 1, len(smaller))

        return (f(nums) - 1) % MOD
