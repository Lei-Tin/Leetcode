class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        count = 2 ** (n - 2)

        if k > count:
            return 1 - self.kthGrammar(n - 1, k - count)
        else:
            return self.kthGrammar(n - 1, k)