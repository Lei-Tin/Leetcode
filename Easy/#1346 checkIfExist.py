class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # for i in range(len(arr) - 1):
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
        #             return True
        #
        # return False

        # Optimized
        s = set()
        for num in arr:

            if num * 2 in s or (num % 2 == 0 and num // 2 in s):
                return True

            s.add(num)

        return False
