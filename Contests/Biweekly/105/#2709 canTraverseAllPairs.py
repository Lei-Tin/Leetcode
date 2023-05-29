# Wasn't able to solve in time
# Learned about prime factorization and how to implement a basic union find
class UF:
    def __init__(self, size):
        self.p = {i: i for i in range(size)}
        self.count = size

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp: return False
        self.p[xp] = yp
        self.count -= 1
        return True


class Solution:
    def factors(self, n: int) -> set:
        ans = set()
        while n % 2 == 0:
            ans.add(2)
            n //= 2

        i = 3
        while i <= int(sqrt(n)):
            while n % i == 0:
                ans.add(i)
                n //= i
            i += 2
        if n > 2:
            ans.add(n)

        return ans

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        n = UF(len(nums))

        primes = {}
        for i in range(len(nums)):
            for prime in self.factors(nums[i]):

                if prime not in primes:
                    primes[prime] = i
                else:
                    n.union(i, primes[prime])

        return n.count == 1
