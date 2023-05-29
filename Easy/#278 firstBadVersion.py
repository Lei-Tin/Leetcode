# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def binary_search(self, start: int, end: int) -> int:
        ver = (start + end) // 2

        if isBadVersion(ver) and isBadVersion(ver - 1) == False:
            return ver

        elif isBadVersion(ver) and isBadVersion(ver - 1):
            # It must be on the left versions list
            return self.binary_search(start, ver - 1)

        else:
            return self.binary_search(ver + 1, end)

    def firstBadVersion(self, n: int) -> int:
        return self.binary_search(1, n)
