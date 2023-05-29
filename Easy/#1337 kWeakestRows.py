class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        lst = []

        for i in range(len(mat)):
            lst.append((self.findFirstZero(mat[i]), i))

        lst = sorted(lst)

        return [lst[i][1] for i in range(k)]

    def findFirstZero(self, lst: List[int]) -> int:
        """Returns the index of the first zero in the list"""
        for i in range(len(lst)):
            if lst[i] == 0:
                return i

        return len(lst)
