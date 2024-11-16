class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def sieve(n):
            primes = [True] * (n + 1)

            for i in range(2, n + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False

            return {i for i in range(2, n + 1) if primes[i]}

        ans = 0

        # Only need to compute until 20 because
        # Max right is 10 ** 6
        # Math log_2(10 ** 6) is 19.93
        primes = sieve(20)

        for num in range(left, right + 1):
            if num.bit_count() in primes:
                ans += 1

        return ans
