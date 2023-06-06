class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # O(n) optimization
        if len(arr) <= 1:
            return True

        smallest = min(arr)
        largest = max(arr)
        n = len(arr)

        if largest == smallest:
            return True

        if (largest - smallest) % (n - 1) != 0:
            return False

        diff = (largest - smallest) / (n - 1)

        if len(set(arr)) != n:
            return False

        return all((num - smallest) % diff == 0 for num in arr)

        # if len(arr) <= 1:
        #     return True

        # else:
        #     arr.sort()
        #     diff = arr[1] - arr[0]

        #     for i in range(len(arr) - 1):
        #         if arr[i + 1] - arr[i] != diff:
        #             return False

        #     return True
