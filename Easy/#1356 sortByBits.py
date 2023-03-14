class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.countOneBit(x), x))

    def countOneBit(self, n: int) -> int:
        """Counts the number of ones bit in this integer n"""
        num = 0
        while n > 0:
            n &= n - 1
            num += 1

        return num
