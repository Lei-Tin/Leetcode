class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Using a binary search for a window of length k
        l = 0
        r = len(arr) - k

        while l < r:
            mid = (l + r) // 2

            # Checking distance
            # x - arr[mid] is distance of the middle item to x
            # arr[mid + k] - x is the distance of the middle + k item to x
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid
            else:
                l = mid + 1

            # mid is the new l we want to set whenever we can find another item
            # that has lesser distance

        return arr[l:l + k]
