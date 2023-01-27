class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return True

        else:
            arr.sort()
            diff = arr[1] - arr[0]

            for i in range(len(arr) - 1):
                if arr[i + 1] - arr[i] != diff:
                    return False

            return True
