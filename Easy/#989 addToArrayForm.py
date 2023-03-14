class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [char for char in str(int(''.join([str(n) for n in num])) + k)]
