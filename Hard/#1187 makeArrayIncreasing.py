class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n, m = len(arr1), len(arr2)

        def binarySearch(arr: List[int], num: int) -> int:
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] > num:
                    r = mid
                elif arr[mid] <= num:
                    l = mid + 1

            return l

        @cache
        def dfs(i: int, j: int, swap: bool) -> int:
            if i >= n:
                return 0

            if swap:
                prev = arr2[j]
            else:
                prev = arr1[j]

            if j == -1:
                prev = -inf

            j = binarySearch(arr2, prev)

            # i is the current index, j is the index in either arr1 or arr2
            swap = 1 + dfs(i + 1, j, True) if j < m else inf
            no_swap = dfs(i + 1, i, False) if arr1[i] > prev else inf

            return min(swap, no_swap)

        ans = dfs(0, -1, False)
        return ans if ans != inf else -1
