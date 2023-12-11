class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n / 4

        count = 0
        curr = -1

        for num in arr:
            if num == curr:
                count += 1
                if count > threshold:
                    return curr

            else:
                curr = num
                count = 1

        return arr[0]
