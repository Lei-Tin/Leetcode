class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        return any(arr[i:i + m] * k == arr[i:i + m * k] for i in range(len(arr) - m * k + 1))
