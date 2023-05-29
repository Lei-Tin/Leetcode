class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # A dictionary mapping the numbers to the amount of appearances in arr1
        mapping = {}

        for num in arr1:
            if num not in mapping:
                mapping[num] = 1

            else:
                mapping[num] += 1

        lst = []

        for num in arr2:
            lst.extend([num] * mapping.pop(num))

        lst2 = []

        for num in mapping:
            lst2.extend([num] * mapping[num])

        return lst + sorted(lst2)
