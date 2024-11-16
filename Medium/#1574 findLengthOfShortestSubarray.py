class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 1
        right = n - 1

        while left < n and arr[left - 1] <= arr[left]:
            left += 1

        if left == n:
            return 0

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        ans = min(n - left, right)

        i = 0
        j = right

        while i < left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
