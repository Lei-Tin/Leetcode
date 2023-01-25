class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        totalSum = 0
        totalProd = 1

        while n > 0:
            rem = n % 10
            totalSum += rem
            totalProd *= rem
            n //= 10

        return totalProd - totalSum
