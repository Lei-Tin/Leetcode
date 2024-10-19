class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        # k is 1 indexed

        # Length of Sn = 2 ** n - 1
        # Finding kth of n is equivalent to
        # If k < 2 ** (n - 1), meaning that this is on the left half
        # If to the left half, don't do anything to k
        if k < 2 ** (n - 1):
            return self.findKthBit(n - 1, k)

        # If k is > 2 ** (n - 1), to the right half
        # It is the reverse of the inverse
        if k > 2 ** (n - 1):
            mapping = {
                '0': '1',
                '1': '0',
            }

            return mapping[self.findKthBit(n - 1, 2 ** n - k)]

        return '1'
