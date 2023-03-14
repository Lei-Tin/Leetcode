class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i + 1) % 2 == 1:
                    ans += sum(arr[i:j + 1])

        return ans
